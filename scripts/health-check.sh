#!/bin/bash
set -e

echo "🏥 Health check CoachLibre services"

NAMESPACE=${1:-"default"}

# Check all deployments
echo "📊 Checking deployments..."
kubectl -n "$NAMESPACE" get deployments

# Check services
echo "🌐 Checking services..."
kubectl -n "$NAMESPACE" get services

# Check ingress
echo "🚪 Checking ingress..."
kubectl -n "$NAMESPACE" get ingress

# Test endpoints
echo "🧪 Testing endpoints..."
DOMAIN=$(kubectl -n "$NAMESPACE" get ingress -o jsonpath='{.items[0].spec.rules[0].host}')

if [ ! -z "$DOMAIN" ]; then
  echo "Testing https://$DOMAIN"
  curl -s -o /dev/null -w "%{http_code}" "https://$DOMAIN" || echo "❌ Frontend not accessible"
  
  echo "Testing https://api.$DOMAIN/api/health"
  curl -s -o /dev/null -w "%{http_code}" "https://api.$DOMAIN/api/health" || echo "❌ Backend not accessible"
fi

echo "✅ Health check completed"
