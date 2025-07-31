#!/bin/bash
set -e

echo "🧪 Testing CoachLibre deployment"

NAMESPACE=${1:-"coachlibre-default"}
DOMAIN=${2:-"coachlibre.dev"}

# Test health endpoints
echo "🏥 Testing health endpoints..."

# Frontend
echo "Testing frontend at https://$DOMAIN"
FRONTEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://$DOMAIN" || echo "000")
if [ "$FRONTEND_STATUS" = "200" ]; then
  echo "✅ Frontend OK"
else
  echo "❌ Frontend failed (status: $FRONTEND_STATUS)"
fi

# Backend
echo "Testing backend at https://api.$DOMAIN/api/health"
BACKEND_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://api.$DOMAIN/api/health" || echo "000")
if [ "$BACKEND_STATUS" = "200" ]; then
  echo "✅ Backend OK"
else
  echo "❌ Backend failed (status: $BACKEND_STATUS)"
fi

# Test Kubernetes resources
echo "🎯 Testing Kubernetes resources..."
kubectl -n "$NAMESPACE" get pods,svc,ing

# Test database connectivity
echo "🗄️ Testing database..."
kubectl -n "$NAMESPACE" exec deployment/payload-backend -- node -e "
const { MongoClient } = require('mongodb');
MongoClient.connect(process.env.DATABASE_URL)
  .then(() => console.log('✅ Database connection OK'))
  .catch(err => { console.log('❌ Database failed:', err.message); process.exit(1); });
"

echo "✅ All tests completed"
