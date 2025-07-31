# CoachLibre MVP - Bootstrap Package

## 🚀 Quick Start

### Local Development
```bash
# 1. Clone repository
git clone https://github.com/your-org/coachlibre-mvp
cd coachlibre-mvp

# 2. Bootstrap local K3s cluster
./scripts/bootstrap-k3s-local.sh

# 3. Create your first tenant
export TENANT_NAME=demo
export TENANT_DOMAIN=demo.coachlibre.dev
./scripts/create-tenant.sh
```

### Remote Production
```bash
# 1. Setup environment variables
export SERVER_IP=your.server.ip
export DOMAIN=coachlibre.com
export CLOUDFLARE_API_TOKEN=your_token

# 2. Bootstrap remote cluster
./scripts/bootstrap-k3s-remote.sh
```

## 🏗️ Architecture

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

## 🎯 Features

- ✅ Multi-tenant SaaS architecture
- ✅ AI-powered coaching assistant
- ✅ Inline site builder (TinaCMS)
- ✅ Video calls (LiveKit)
- ✅ Workflow automation (n8n)
- ✅ GitOps deployment (ArgoCD)
- ✅ Auto DNS management (Cloudflare)

## 🔧 Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Astro + React Islands |
| Backend | PayloadCMS + Node.js |
| Database | PostgreSQL + Qdrant |
| AI | Flowise + Ollama |
| Workflow | n8n + CrewAI |
| Video | LiveKit |
| DevOps | K3s + ArgoCD + Helm |
| DNS | Cloudflare API |

## 📚 Next Steps

1. Customize `config/tenant-wizard.yml` for your needs
2. Add your integrations (Stripe, Google Calendar, etc.)
3. Deploy additional environments (staging/prod)
4. Scale with Crossplane for multi-cluster

## 🆘 Support

- 📖 [Full Documentation](./docs/)
- 🐛 [Issue Tracker](https://github.com/your-org/coachlibre-mvp/issues)
- 💬 [Discord Community](https://discord.gg/coachlibre)
