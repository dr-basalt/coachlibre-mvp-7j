# 🚀 CoachLibre MVP - Bootstrap Complet

Plateforme SaaS de coaching avec IA intégrée, architecture multi-tenant, et déploiement automatisé sur Kubernetes.

## ✨ Fonctionnalités

- 🤖 **IA intégrée** : Assistant conversationnel avec Flowise + CrewAI + Qdrant  
- 🏗️ **Site Builder** : Edition inline avec TinaCMS + templates
- 📹 **Visioconférence** : LiveKit WebRTC → HLS scaling
- 🔄 **Workflows** : Automatisation n8n + agents CrewAI métiers
- 🌐 **Multi-tenant** : Isolation complète + DNS automatique
- 🔧 **GitOps** : Déploiement ArgoCD + Helm + Crossplane
- 📊 **Monitoring** : Prometheus + Grafana intégrés

## 🎯 Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Astro Site    │    │  PayloadCMS     │    │   Flowise AI    │
│   (Frontend)    │◄──►│   (Backend)     │◄──►│  (Workflows)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │   PostgreSQL    │
                    │    + Qdrant     │
                    └─────────────────┘
```

## 🚀 Démarrage Rapide

### Local (Développement)
```bash
git clone https://github.com/your-org/coachlibre-mvp
cd coachlibre-mvp

# Bootstrap K3s local
./scripts/bootstrap-k3s-local.sh

# Créer votre premier tenant
export TENANT_NAME=demo
export TENANT_DOMAIN=demo.coachlibre.dev
./scripts/create-tenant.sh
```

### Production (Hetzner/Oracle)
```bash
# Configuration
export SERVER_IP=your.server.ip
export DOMAIN=coachlibre.com
export CLOUDFLARE_API_TOKEN=your_token

# Déploiement
./scripts/bootstrap-k3s-remote.sh

# Configuration secrets
./scripts/setup-secrets.sh coachlibre-prod production

# Test de santé
./scripts/health-check.sh coachlibre-prod
```

## 📦 Stack Technique

| Composant | Technologie | Port | Description |
|-----------|-------------|------|-------------|
| **Frontend** | Astro + React | 3000 | Site vitrine + SPA |
| **Backend** | PayloadCMS | 3001 | API + Admin CMS |
| **IA** | Flowise + Qdrant | 3002/6333 | Assistant + RAG |
| **Workflows** | n8n + CrewAI | 5678 | Automatisation |
| **Video** | LiveKit | 7880 | Visioconférence |
| **Database** | PostgreSQL | 5432 | Données principales |

## 🎮 Commandes Utiles

```bash
# 🔍 Status du cluster
kubectl get pods,svc,ing -A

# 📊 Monitoring
kubectl port-forward -n monitoring svc/grafana 3000:80

# 🧪 Tests
./scripts/test-deployment.sh coachlibre-prod

# 💾 Backup
./scripts/backup-tenant.sh demo-tenant

# 🌐 DNS Cloudflare
python3 scripts/cloudflare-dns.py --action create-tenant --domain demo.coachlibre.com --ip 1.2.3.4
```

## 🏗️ Structure Projet

```
coachlibre-mvp/
├── 🔄 .github/workflows/      # CI/CD GitHub Actions
├── 📱 applications/           # Code source applications
├── ⚙️ config/                 # Configurations & templates
├── 📦 helm-charts/            # Charts Helm par service
├── 🏗️ infrastructure/         # Infrastructure as Code
├── 📋 scripts/               # Scripts d'automatisation
└── 📚 docs/                  # Documentation complète
```

## 🎯 Prochaines Étapes

1. **Personnaliser** `config/tenant-wizard.yml`
2. **Configurer** secrets GitHub Actions
3. **Déployer** premier tenant test
4. **Intégrer** services externes (Stripe, Google Cal, etc.)
5. **Scaler** avec Crossplane multi-cluster

## 🆘 Support

- 📖 [Documentation](./docs/)
- 🐛 [Issues](https://github.com/your-org/coachlibre-mvp/issues)  
- 💬 [Discord](https://discord.gg/coachlibre)

---

**CoachLibre MVP** - De l'idée à la production en quelques minutes ! 🚀
