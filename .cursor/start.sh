#!/usr/bin/env bash
# Per-boot startup for the Restack AI Python examples.
# Brings up the Docker daemon and the shared Restack engine container that
# every example connects to, plus the local Ollama server used by the
# fully-offline agent example. Idempotent: safe to run on each boot.
set -euo pipefail

# --- Docker daemon -----------------------------------------------------------
if ! sudo docker info >/dev/null 2>&1; then
  sudo service docker start || true
  for _ in $(seq 1 30); do
    sudo docker info >/dev/null 2>&1 && break
    sleep 1
  done
fi

# --- Ollama server (local LLM for the offline agent example) -----------------
if command -v ollama >/dev/null 2>&1 \
   && ! curl -sf http://localhost:11434/api/version >/dev/null 2>&1; then
  nohup ollama serve >/tmp/ollama.log 2>&1 &
  for _ in $(seq 1 30); do
    curl -sf http://localhost:11434/api/version >/dev/null 2>&1 && break
    sleep 1
  done
fi

# --- Restack engine container ------------------------------------------------
# UI :5233  API :6233  temporal :7233  stream :9233  operator :10233
if sudo docker ps -a --format '{{.Names}}' | grep -qx restack; then
  sudo docker start restack || true
else
  sudo docker run -d --name restack \
    -p 5233:5233 -p 6233:6233 -p 7233:7233 -p 9233:9233 -p 10233:10233 \
    ghcr.io/restackio/restack:main
fi

# --- Wait for the Developer UI to be reachable -------------------------------
for _ in $(seq 1 60); do
  if curl -sf -o /dev/null http://localhost:5233; then
    echo "Restack engine is ready at http://localhost:5233"
    exit 0
  fi
  sleep 2
done

echo "Restack engine did not become ready in time" >&2
exit 1
