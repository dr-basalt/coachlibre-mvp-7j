#!/bin/bash
set -e

echo "🏢 Creating new CoachLibre tenant"

# Read tenant configuration
TENANT_CONFIG=${1:-"config/tenant-wizard.yml"}

# Parse YAML and create tenant resources
yq eval '.tenant.name' $TENANT_CONFIG
yq eval '.tenant.domain' $TENANT_CONFIG

# Apply tenant-specific configurations
envsubst < infrastructure/argocd/bootstrap/tenant-template.yml | kubectl apply -f -

echo "✅ Tenant created successfully!"
