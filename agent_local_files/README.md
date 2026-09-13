# Restack AI - Offline agent over local files (Ollama + RAG)

A fully **offline** AI agent that reasons over your **local files** using **local
models** only. It combines:

- **Local intelligence** — `llama3.1:8b` (strong, reliable chat + tool calling)
  served by Ollama.
- **A local knowledge base** — text files under `knowledge/` are embedded with
  the local `nomic-embed-text` model into an on-disk vector index, and searched
  with retrieval-augmented generation (RAG).
- **Local file tools** — the agent can list, read, and write files on disk.

No OpenAI key and no internet access are required at runtime; nothing leaves the
machine.

## Prerequisites

- Docker (for running Restack)
- Python 3.10 or higher
- [Ollama](https://ollama.com)

## 1. Install Ollama and pull the models

```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama serve &
ollama pull llama3.1:8b        # chat + tool calling (~4.9 GB)
ollama pull nomic-embed-text   # embeddings for the knowledge base (~275 MB)
```

## 2. Start Restack

```bash
docker run -d --pull always --name restack -p 5233:5233 -p 6233:6233 -p 7233:7233 -p 9233:9233 -p 10233:10233 ghcr.io/restackio/restack:main
```

## 3. Install dependencies and run the service

```bash
uv sync
uv run services
```

## 4. (Optional) Build the index up-front

The index is built automatically on first search, but you can pre-build it:

```bash
uv run ingest
```

## 5. Ask the agent (offline, end-to-end)

```bash
uv run schedule
```

This asks the agent to explain — using only the local knowledge base — how the
project runs offline and how the knowledge base works, then to **write a summary
to `workspace/summary.md`**. The agent searches the local index, reads files,
composes an answer, and writes the file, all via the local models.

## What the agent knows and can do

| Aspect | Details |
| --- | --- |
| Intelligence | Local `llama3.1:8b` via Ollama (OpenAI-compatible API) |
| Knowledge base | On-disk vector index over `knowledge/` (embeddings via `nomic-embed-text`) |
| Tools | `search_knowledge` (RAG), `list_files`, `read_file`, `write_file` |
| Storage | Vector index in `.index/`; files read from the project, written to `workspace/` |

### Add your own files

Drop any `.md`, `.txt`, `.py`, `.json`, or `.yaml` files into `knowledge/` (or
set `KNOWLEDGE_DIR` to another local folder). The index rebuilds automatically
when the files change, so the agent immediately reasons over your content.

## How it works

`src/knowledge_base.py` chunks each file, embeds the chunks with the local
embedding model, and stores an embeddings matrix plus metadata under `.index/`.
`search_knowledge` embeds the query and ranks chunks by cosine similarity,
returning the top matches with their source file. The agent
(`src/agents/agent_local_files.py`) runs a small tool-calling loop: it searches
and reads local files, then answers and optionally writes a file — entirely with
local models.

File access is sandboxed: reads/listing are confined to the project root and
writes are confined to the `workspace/` directory.
