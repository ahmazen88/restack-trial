#!/usr/bin/env bash
# Idempotent repository setup for the Restack AI Python examples.
# Installs the Docker engine (used to run the Restack service), the
# fuse-overlayfs storage driver required inside the nested Cloud Agent VM,
# and the uv Python package manager. Also pre-syncs the child_workflows
# quickstart so it is ready to run out of the box.
set -euo pipefail

export DEBIAN_FRONTEND=noninteractive

# --- Docker engine -----------------------------------------------------------
if ! command -v docker >/dev/null 2>&1; then
  curl -fsSL https://get.docker.com | sudo sh
fi

# fuse-overlayfs: overlay2/native overlay mounts fail inside the nested
# container, so Docker must use the FUSE-based storage driver instead.
sudo apt-get update -y
sudo apt-get install -y --no-install-recommends fuse-overlayfs
# The fuse3 package ships an interactive conffile prompt; keep the existing file.
sudo dpkg --configure -a --force-confold || true

sudo mkdir -p /etc/docker
echo '{"storage-driver":"fuse-overlayfs"}' | sudo tee /etc/docker/daemon.json >/dev/null
sudo usermod -aG docker "$USER" || true

# --- uv (Python package/venv manager) ---------------------------------------
if [ ! -x "$HOME/.local/bin/uv" ] && ! command -v uv >/dev/null 2>&1; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi
export PATH="$HOME/.local/bin:$PATH"

# --- Pre-sync the quickstart example ----------------------------------------
uv sync --project child_workflows

echo "install.sh completed successfully"
