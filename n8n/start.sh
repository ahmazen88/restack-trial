#!/usr/bin/env bash
# Start Community n8n locally. No n8n Cloud account.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

N8N_VERSION="${N8N_VERSION:-2.40.7}"
export N8N_USER_FOLDER="${N8N_USER_FOLDER:-$ROOT/.n8n-data}"
export N8N_HOST="${N8N_HOST:-localhost}"
export N8N_PORT="${N8N_PORT:-5678}"
export N8N_PROTOCOL="${N8N_PROTOCOL:-http}"
export N8N_SECURE_COOKIE="${N8N_SECURE_COOKIE:-false}"
export N8N_DIAGNOSTICS_ENABLED="${N8N_DIAGNOSTICS_ENABLED:-false}"
export N8N_PERSONALIZATION_ENABLED="${N8N_PERSONALIZATION_ENABLED:-false}"
export N8N_VERSION_NOTIFICATIONS_ENABLED="${N8N_VERSION_NOTIFICATIONS_ENABLED:-false}"
export N8N_HIRING_BANNER_ENABLED="${N8N_HIRING_BANNER_ENABLED:-false}"

# Load KEY=VALUE without bash-expanding bcrypt hashes ($2b$10$...).
load_env_file() {
  local file="$1" line key value
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" || "$line" =~ ^[[:space:]]*# ]] && continue
    key="${line%%=*}"
    value="${line#*=}"
    if [[ "$value" == \'*\' || "$value" == \"*\" ]]; then
      value="${value:1:-1}"
    fi
    export "${key}=${value}"
  done < "$file"
}

if [[ -f "$ROOT/.local-owner.env" ]]; then
  load_env_file "$ROOT/.local-owner.env"
fi

if [[ -n "${N8N_INSTANCE_OWNER_PASSWORD_HASH:-}" ]]; then
  export N8N_INSTANCE_OWNER_MANAGED_BY_ENV="${N8N_INSTANCE_OWNER_MANAGED_BY_ENV:-true}"
  export N8N_INSTANCE_OWNER_EMAIL="${N8N_INSTANCE_OWNER_EMAIL:-local@n8n.local}"
  export N8N_INSTANCE_OWNER_FIRST_NAME="${N8N_INSTANCE_OWNER_FIRST_NAME:-Local}"
  export N8N_INSTANCE_OWNER_LAST_NAME="${N8N_INSTANCE_OWNER_LAST_NAME:-Owner}"
  export N8N_INSTANCE_OWNER_PASSWORD_HASH
fi

mkdir -p "$N8N_USER_FOLDER"
echo "Starting n8n ${N8N_VERSION} at ${N8N_PROTOCOL}://${N8N_HOST}:${N8N_PORT}"
echo "Data folder: ${N8N_USER_FOLDER}"
exec npx --yes "n8n@${N8N_VERSION}"
