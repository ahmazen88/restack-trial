#!/usr/bin/env bash
# Start Community n8n locally. No n8n Cloud account.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"

N8N_VERSION="${N8N_VERSION:-2.40.7}"
NODE24_VERSION="${NODE24_VERSION:-24.21.0}"
NODE_HOME="${NODE_HOME:-$ROOT/.n8n-node}"

node_major() {
  node -p 'process.versions.node.split(".")[0]' 2>/dev/null || echo 0
}

ensure_node24() {
  if [[ "$(node_major)" -ge 24 ]]; then
    return 0
  fi
  if [[ -x "$NODE_HOME/bin/node" ]]; then
    export PATH="$NODE_HOME/bin:$PATH"
    return 0
  fi
  local archive="node-v${NODE24_VERSION}-linux-x64"
  local url="https://nodejs.org/dist/v${NODE24_VERSION}/${archive}.tar.xz"
  echo "n8n ${N8N_VERSION} needs Node 24+. Installing ${archive} into ${NODE_HOME}"
  local tmp
  tmp="$(mktemp -d)"
  curl -fsSL "$url" -o "$tmp/node.tar.xz"
  tar -xJf "$tmp/node.tar.xz" -C "$tmp"
  rm -rf "$NODE_HOME"
  mv "$tmp/$archive" "$NODE_HOME"
  rm -rf "$tmp"
  export PATH="$NODE_HOME/bin:$PATH"
}

ensure_node24
echo "Node $(node -v) ($(command -v node))"

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
