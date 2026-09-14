#!/usr/bin/env bash
# One-command launcher for the fully offline Local Files chat UI.
#
# Brings up everything a non-technical user needs on a fresh machine:
#   1. Docker daemon + the shared Restack engine container
#   2. the local Ollama server (local LLM + embeddings)
#   3. the AgentLocalFiles worker (uv run services)
#   4. the chat web server (uv run serve) on http://localhost:8000
# Then it waits for the page to respond and opens a browser if one is available.
#
# Safe to re-run: each step is skipped when it is already up.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
export PATH="$HOME/.local/bin:$PATH"

WORKER_LOG="/tmp/local_files_worker.log"
WEBUI_LOG="/tmp/local_files_webui.log"
CHAT_URL="http://localhost:8000"

cd "$SCRIPT_DIR"

echo "==> Starting Docker engine, Restack, and Ollama (this may take a moment)…"
bash "$REPO_ROOT/.cursor/start.sh"

# --- Ollama server (belt-and-suspenders; start.sh already handles this) ------
# Keep models resident between requests to avoid slow CPU reloads per call.
export OLLAMA_KEEP_ALIVE="${OLLAMA_KEEP_ALIVE:--1}"
if command -v ollama >/dev/null 2>&1 \
   && ! curl -sf http://localhost:11434/api/version >/dev/null 2>&1; then
  echo "==> Starting Ollama server…"
  nohup ollama serve >/tmp/ollama.log 2>&1 &
  for _ in $(seq 1 30); do
    curl -sf http://localhost:11434/api/version >/dev/null 2>&1 && break
    sleep 1
  done
fi

# --- Agent worker ------------------------------------------------------------
if pgrep -f "agent_local_files/.venv/bin/services" >/dev/null 2>&1; then
  echo "==> Agent worker already running."
else
  echo "==> Starting the AgentLocalFiles worker…"
  nohup uv run services >"$WORKER_LOG" 2>&1 &
  for _ in $(seq 1 30); do
    grep -q "Service on task queue restack ready" "$WORKER_LOG" 2>/dev/null && break
    sleep 1
  done
fi

# --- Chat web server ---------------------------------------------------------
if curl -sf -o /dev/null "$CHAT_URL" 2>/dev/null; then
  echo "==> Chat web server already running."
else
  echo "==> Starting the chat web server…"
  nohup uv run serve >"$WEBUI_LOG" 2>&1 &
fi

echo "==> Waiting for the chat page to become ready…"
for _ in $(seq 1 60); do
  if curl -sf -o /dev/null "$CHAT_URL"; then
    echo ""
    echo "  ✅ Your offline assistant is ready!"
    echo "  👉 Open this page in your browser:  $CHAT_URL"
    echo ""
    # Best-effort: open a browser if a desktop is available.
    (xdg-open "$CHAT_URL" >/dev/null 2>&1 \
      || google-chrome "$CHAT_URL" >/dev/null 2>&1 \
      || python3 -m webbrowser "$CHAT_URL" >/dev/null 2>&1) &
    exit 0
  fi
  sleep 2
done

echo "The chat server did not become ready in time. See $WEBUI_LOG" >&2
exit 1
