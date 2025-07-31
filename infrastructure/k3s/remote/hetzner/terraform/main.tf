terraform {
  required_version = ">= 1.0"
  required_providers {
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.44"
    }
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 4.0"
    }
  }
}

provider "hcloud" {
  token = var.hcloud_token
}

provider "cloudflare" {
  api_token = var.cloudflare_api_token
}

variable "hcloud_token" {
  description = "Hetzner Cloud API Token"
  type        = string
  sensitive   = true
}

variable "cloudflare_api_token" {
  description = "Cloudflare API Token"
  type        = string
  sensitive   = true
}

variable "cluster_name" {
  description = "Name of the K3s cluster"
  type        = string
  default     = "coachlibre-prod"
}

variable "domain" {
  description = "Base domain for the cluster"
  type        = string
}

# Création du serveur Hetzner
resource "hcloud_server" "k3s_master" {
  name         = "${var.cluster_name}-master"
  image        = "ubuntu-22.04"
  server_type  = "cx21"  # 2 vCPU, 4GB RAM
  location     = "nbg1"  # Nuremberg
  ssh_keys     = [hcloud_ssh_key.default.id]
  
  user_data = templatefile("${path.module}/../cloud-init.yml", {
    SSH_PUBLIC_KEY = file("~/.ssh/id_rsa.pub")
  })
  
  public_net {
    ipv4_enabled = true
    ipv6_enabled = false
  }
  
  labels = {
    role        = "master"
    environment = "production"
    project     = "coachlibre"
  }
}

resource "hcloud_ssh_key" "default" {
  name       = "${var.cluster_name}-key"
  public_key = file("~/.ssh/id_rsa.pub")
}

# Volume pour persistance
resource "hcloud_volume" "k3s_storage" {
  name      = "${var.cluster_name}-storage"
  size      = 50
  server_id = hcloud_server.k3s_master.id
  automount = true
  format    = "ext4"
}

# Enregistrements DNS Cloudflare
data "cloudflare_zone" "main" {
  name = var.domain
}

resource "cloudflare_record" "k3s_master" {
  zone_id = data.cloudflare_zone.main.id
  name    = "k3s"
  value   = hcloud_server.k3s_master.ipv4_address
  type    = "A"
  ttl     = 300
}

resource "cloudflare_record" "wildcard" {
  zone_id = data.cloudflare_zone.main.id
  name    = "*"
  value   = hcloud_server.k3s_master.ipv4_address
  type    = "A"
  ttl     = 300
}

# Outputs
output "server_ip" {
  value = hcloud_server.k3s_master.ipv4_address
}

output "server_name" {
  value = hcloud_server.k3s_master.name
}
