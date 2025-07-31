# Architecture CoachLibre MVP

## Vue d'ensemble

```mermaid
graph TB
    A[Client Browser] --> B[Traefik Ingress]
    B --> C[Astro Frontend]
    B --> D[PayloadCMS Backend]
    B --> E[Flowise AI]
    B --> F[n8n Workflows]
    B --> G[LiveKit Video]
    
    C --> H[TinaCMS Builder]
    D --> I[PostgreSQL]
    E --> J[Qdrant Vector DB]
    F --> K[Redis Cache]
    
    L[ArgoCD] --> M[Helm Charts]
    M --> N[K8s Resources]
```

## Stack Technique

| Composant | Technologie | Rôle |
|-----------|-------------|------|
| Frontend | Astro + React | Site vitrine + SPA |
| CMS | PayloadCMS | API + Admin |
| IA | Flowise + Qdrant | Assistant conversationnel |
| Workflows | n8n + CrewAI | Automatisation métier |
| Video | LiveKit | Visioconférence |
| Orchestration | K3s + ArgoCD | Container + GitOps |
| Monitoring | Prometheus + Grafana | Observabilité |

## Flux de Données

1. **Utilisateur** → Frontend Astro
2. **Frontend** → API PayloadCMS
3. **API** → Base PostgreSQL
4. **IA** → Qdrant (RAG) + Flowise
5. **Workflows** → n8n → Intégrations externes

## Sécurité

- TLS automatique (cert-manager)
- WAF Cloudflare
- RBAC Kubernetes
- Secrets management
