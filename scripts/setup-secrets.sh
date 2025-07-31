#!/bin/bash
set -e

echo "🔐 Setting up Kubernetes secrets for CoachLibre"

NAMESPACE=${1:-"default"}
ENVIRONMENT=${2:-"development"}

# Load environment variables
source "config/environment-templates/${ENVIRONMENT}.env"

# Create namespace if it doesn't exist
kubectl create namespace "$NAMESPACE" --dry-run=client -o yaml | kubectl apply -f -

# Create generic secrets
kubectl -n "$NAMESPACE" create secret generic coachlibre-secrets \
  --from-literal=payload-secret="$PAYLOAD_SECRET" \
  --from-literal=database-url="$DATABASE_URL" \
  --from-literal=openai-api-key="$OPENAI_API_KEY" \
  --from-literal=cloudflare-api-token="$CLOUDFLARE_API_TOKEN" \
  --dry-run=client -o yaml | kubectl apply -f -

# Create TLS secrets for ingress
kubectl -n "$NAMESPACE" create secret tls coachlibre-tls \
  --cert=path/to/tls.crt \
  --key=path/to/tls.key \
  --dry-run=client -o yaml | kubectl apply -f -

echo "✅ Secrets created in namespace: $NAMESPACE"
