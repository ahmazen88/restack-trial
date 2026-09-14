# Running agents fully offline with Ollama

Ollama runs large language models locally and exposes an OpenAI-compatible API
at http://localhost:11434/v1. Because it speaks the same protocol as OpenAI,
existing agent code can talk to it by only changing the base URL and using a
dummy API key.

This project uses two local models:

- llama3.1:8b: a chat model that supports tool calling. It powers the agent's
  reasoning and decides which tools to call.
- nomic-embed-text: an embedding model that turns text into 768-dimensional
  vectors. It powers semantic search over the local knowledge base.

No data leaves the machine: there is no OpenAI API key and no internet access is
required at runtime. This makes the setup suitable for air-gapped or
privacy-sensitive environments.
