# scripts/bootstrap-k3s-local.sh
#!/bin/bash
set -e

echo "🚀 Bootstrap CoachLibre MVP - K3s Local"

# Variables
CLUSTER_NAME=${CLUSTER_NAME:-"coachlibre-local"}
KUBECONFIG_PATH=${KUBECONFIG_PATH:-"$HOME/.kube/config-coachlibre"}

# 1. Install K3s with Traefik disabled (we'll use our own)
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--disable traefik --write-kubeconfig-mode 644" sh -

# 2. Wait for K3s to be ready
echo "⏳ Waiting for K3s to be ready..."
kubectl wait --for=condition=Ready nodes --all --timeout=300s

# 3. Install Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# 4. Add Helm repositories
helm repo add traefik https://helm.traefik.io/traefik
helm repo add argo https://argoproj.github.io/argo-helm
helm repo add jetstack https://charts.jetstack.io
helm repo update

# 5. Install Traefik
kubectl create namespace traefik-system || true
helm install traefik traefik/traefik \
  --namespace traefik-system \
  --values infrastructure/k3s/local/traefik-config.yml

# 6. Install cert-manager
kubectl create namespace cert-manager || true
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --set installCRDs=true

# 7. Install ArgoCD
kubectl create namespace argocd || true
helm install argocd argo/argo-cd \
  --namespace argocd \
  --values infrastructure/argocd/bootstrap/argocd-install.yml

# 8. Wait for ArgoCD to be ready
kubectl wait --for=condition=available deployment/argocd-server -n argocd --timeout=300s

# 9. Bootstrap applications
kubectl apply -f infrastructure/argocd/bootstrap/app-of-apps.yml

echo "✅ K3s cluster ready! Access ArgoCD at: https://argocd.local.coachlibre.dev"
echo "Default admin password:"
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
