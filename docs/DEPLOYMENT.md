# Guide de Déploiement CoachLibre MVP

## 🚀 Déploiement Rapide

### Prérequis
- Cluster Kubernetes (K3s recommandé)
- Helm 3.x
- kubectl configuré
- Docker Hub account
- Domaine avec accès DNS (Cloudflare recommandé)

### Installation Local

```bash
# 1. Cloner le repository
git clone https://github.com/your-org/coachlibre-mvp
cd coachlibre-mvp

# 2. Bootstrap K3s local
./scripts/bootstrap-k3s-local.sh

# 3. Créer votre premier tenant
export TENANT_NAME=demo
export TENANT_DOMAIN=demo.coachlibre.dev
./scripts/create-tenant.sh
```

### Installation Production

```bash
# 1. Configurer les variables
export SERVER_IP=your.server.ip
export DOMAIN=coachlibre.com
export CLOUDFLARE_API_TOKEN=your_token

# 2. Déployer sur serveur distant
./scripts/bootstrap-k3s-remote.sh

# 3. Configurer les secrets
./scripts/setup-secrets.sh coachlibre-prod production

# 4. Test de santé
./scripts/health-check.sh coachlibre-prod
```

## 🔧 Configuration

### Variables d'Environnement

Copier et personnaliser les templates :
- `config/environment-templates/development.env`
- `config/environment-templates/staging.env`
- `config/environment-templates/production.env`

### DNS Cloudflare

Configuration automatique via `config/cloudflare-config.yml`

### Monitoring

Stack Prometheus + Grafana déployée via ArgoCD :
- Grafana : https://grafana.votre-domaine.com
- Prometheus : https://prometheus.votre-domaine.com
