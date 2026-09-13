#!/usr/bin/env bash
# Idempotent repository setup for the Restack AI Python examples.
# Installs the Docker engine (used to run the Restack service), the
# fuse-overlayfs storage driver required inside the nested Cloud Agent VM,
# the uv Python package manager, and Ollama with a local model so the
# fully-offline agent example (agent_ollama) works without any API key.
# Also pre-syncs the child_workflows and agent_ollama examples.
set -euo pipefail

export DEBIAN_FRONTEND=noninteractive

# Local models for the offline agent examples:
#   - llama3.2: chat + tool calling
#   - nomic-embed-text: embeddings for the local-files knowledge base (RAG)
OLLAMA_MODEL="${OLLAMA_MODEL:-llama3.2}"
OLLAMA_EMBED_MODEL="${OLLAMA_EMBED_MODEL:-nomic-embed-text}"

# --- Docker engine -----------------------------------------------------------
if ! command -v docker >/dev/null 2>&1; then
  curl -fsSL https://get.docker.com | sudo sh
fi

# fuse-overlayfs: overlay2/native overlay mounts fail inside the nested
# container, so Docker must use the FUSE-based storage driver instead.
# zstd is required by the Ollama installer to unpack its release archive.
# fuse3 ships an interactive /etc/fuse.conf conffile prompt that DEBIAN_FRONTEND
# does not suppress, so force-keep the existing conffile to stay non-interactive.
sudo apt-get update -y
sudo apt-get install -y --no-install-recommends \
  -o Dpkg::Options::=--force-confdef \
  -o Dpkg::Options::=--force-confold \
  fuse-overlayfs zstd
sudo dpkg --configure -a --force-confdef --force-confold || true

sudo mkdir -p /etc/docker
echo '{"storage-driver":"fuse-overlayfs"}' | sudo tee /etc/docker/daemon.json >/dev/null
sudo usermod -aG docker "$USER" || true

# --- uv (Python package/venv manager) ---------------------------------------
if [ ! -x "$HOME/.local/bin/uv" ] && ! command -v uv >/dev/null 2>&1; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi
export PATH="$HOME/.local/bin:$PATH"

# --- Ollama (local LLM for the fully-offline agent example) ------------------
if ! command -v ollama >/dev/null 2>&1; then
  curl -fsSL https://ollama.com/install.sh | sh
fi

# Pulling a model needs a running server; start a temporary one if needed.
# The downloaded model is stored on disk and persists into the snapshot.
ollama_pid=""
if ! curl -sf http://localhost:11434/api/version >/dev/null 2>&1; then
  nohup ollama serve >/tmp/ollama-install.log 2>&1 &
  ollama_pid="$!"
  for _ in $(seq 1 30); do
    curl -sf http://localhost:11434/api/version >/dev/null 2>&1 && break
    sleep 1
  done
fi

for model in "${OLLAMA_MODEL}" "${OLLAMA_EMBED_MODEL}"; do
  if ! ollama list | awk '{print $1}' | grep -q "^${model}"; then
    ollama pull "${model}"
  fi
done

# Stop the temporary server (by PID); start.sh manages it on each boot.
if [ -n "${ollama_pid}" ]; then
  kill "${ollama_pid}" 2>/dev/null || true
fi

# --- Pre-sync the example projects -------------------------------------------
uv sync --project child_workflows
uv sync --project agent_ollama
uv sync --project agent_local_files

echo "install.sh completed successfully"
