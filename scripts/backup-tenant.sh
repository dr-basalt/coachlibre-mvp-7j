#!/bin/bash
set -e

echo "💾 Backup tenant data"

TENANT_NAME=${1:-"default"}
BACKUP_PATH=${2:-"/tmp/coachlibre-backups"}
DATE=$(date +%Y%m%d_%H%M%S)

# Create backup directory
mkdir -p "$BACKUP_PATH/$TENANT_NAME"

# Backup database
echo "📊 Backing up database..."
kubectl exec -n "$TENANT_NAME" deployment/postgres -- pg_dump \
  -U postgres coachlibre > "$BACKUP_PATH/$TENANT_NAME/db_$DATE.sql"

# Backup persistent volumes
echo "💿 Backing up volumes..."
kubectl get pv -o yaml > "$BACKUP_PATH/$TENANT_NAME/pv_$DATE.yaml"

# Backup configurations
echo "⚙️ Backing up configurations..."
kubectl get configmaps,secrets -n "$TENANT_NAME" -o yaml > "$BACKUP_PATH/$TENANT_NAME/config_$DATE.yaml"

# Create archive
echo "📦 Creating archive..."
tar -czf "$BACKUP_PATH/coachlibre_${TENANT_NAME}_$DATE.tar.gz" \
  -C "$BACKUP_PATH" "$TENANT_NAME"

echo "✅ Backup completed: $BACKUP_PATH/coachlibre_${TENANT_NAME}_$DATE.tar.gz"
