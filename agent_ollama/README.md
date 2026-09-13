# Restack AI - Fully offline agent (Ollama)

This example is a tool-calling AI agent that runs **completely offline**. Instead
of calling OpenAI, the agent talks to a local [Ollama](https://ollama.com) server
through its OpenAI-compatible API, so no external API key and no internet access
are required at runtime.

It is a drop-in offline variant of the [`agent_tool`](../agent_tool) example: the
agent answers questions about sales data and uses a `lookup_sales` tool to fetch
the data.

## Prerequisites

- Docker (for running Restack)
- Python 3.10 or higher
- [Ollama](https://ollama.com) installed locally

## 1. Install Ollama and pull a model

```bash
# Install Ollama (Linux)
curl -fsSL https://ollama.com/install.sh | sh

# Start the Ollama server (keep this running)
ollama serve &

# Download a tool-capable model (~2 GB)
ollama pull llama3.2
```

`llama3.2` supports tool calling, which this agent relies on. You can point the
agent at any other tool-capable model with the `OLLAMA_MODEL` env var.

## 2. Start Restack

```bash
docker run -d --pull always --name restack -p 5233:5233 -p 6233:6233 -p 7233:7233 -p 9233:9233 -p 10233:10233 ghcr.io/restackio/restack:main
```

The Developer UI is available at http://localhost:5233

## 3. Configure environment variables

Duplicate `.env.example` to `.env` (the defaults already point at a local Ollama
server, so no changes are needed for a standard setup):

```bash
cp .env.example .env
```

| Variable | Default | Description |
| --- | --- | --- |
| `OLLAMA_BASE_URL` | `http://localhost:11434/v1` | Ollama OpenAI-compatible endpoint |
| `OLLAMA_MODEL` | `llama3.2` | Local model used by the agent |

## 4. Install dependencies and run the service

If using uv:

```bash
uv sync
uv run services
```

If using pip:

```bash
pip install -e .
python -c "from src.services import run_services; run_services()"
```

## 5. Run the agent

### From any client (offline, end-to-end)

```bash
uv run schedule
```

`schedule.py` schedules the `AgentOllama` agent, sends a user message
(`"What apparel is currently on sale?"`), prints the assistant's reply, and ends
the run — all served by the local model.

### From the API

```bash
# Create an agent run
POST http://localhost:6233/api/agents/AgentOllama

# Send a message to the run
PUT http://localhost:6233/api/agents/AgentOllama/:agentId/:runId
{
  "eventName": "messages",
  "eventInput": {
    "messages": [{ "role": "user", "content": "What apparel is currently on sale?" }]
  }
}
```

### From the UI

Open http://localhost:5233, run the `AgentOllama` agent, and send a `messages`
event from the timeline.

## How the offline wiring works

`src/functions/llm_chat.py` creates an OpenAI client pointed at the local Ollama
server:

```python
client = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")  # api_key ignored by Ollama
```

Because Ollama implements the OpenAI Chat Completions API (including `tools`), the
rest of the agent code is identical to the OpenAI-backed example.
