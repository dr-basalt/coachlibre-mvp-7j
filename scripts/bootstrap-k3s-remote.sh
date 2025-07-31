# scripts/bootstrap-k3s-remote.sh
#!/bin/bash
set -e

echo "🌐 Bootstrap CoachLibre MVP - K3s Remote"

# Variables
PROVIDER=${PROVIDER:-"hetzner"} # hetzner or oracle
SERVER_IP=${SERVER_IP}
DOMAIN=${DOMAIN}
CLOUDFLARE_API_TOKEN=${CLOUDFLARE_API_TOKEN}

if [[ -z "$SERVER_IP" || -z "$DOMAIN" || -z "$CLOUDFLARE_API_TOKEN" ]]; then
  echo "❌ Required variables: SERVER_IP, DOMAIN, CLOUDFLARE_API_TOKEN"
  exit 1
fi

# 1. Setup DNS
echo "🌐 Setting up DNS..."
python3 scripts/cloudflare-dns.py --action create --domain "$DOMAIN" --ip "$SERVER_IP"

# 2. Connect to remote server and install K3s
ssh root@$SERVER_IP << 'EOF'
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--disable traefik --tls-san $(curl -s ifconfig.me)" sh -
EOF

# 3. Copy kubeconfig
scp root@$SERVER_IP:/etc/rancher/k3s/k3s.yaml ~/.kube/config-coachlibre-remote
sed -i "s/127.0.0.1/$SERVER_IP/" ~/.kube/config-coachlibre-remote

# 4. Continue with helm installations (similar to local script)
echo "✅ Remote K3s cluster ready!"
