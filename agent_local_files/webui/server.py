"""A tiny, friendly chat web UI for the fully offline local-files agent.

FastAPI serves a single-page chat UI and relays messages to the already-running
``AgentLocalFiles`` worker through the Restack client. Everything stays local:
the agent reasons with local Ollama models over the local knowledge base, so no
OpenAI key and no internet access are needed at runtime.
"""

from __future__ import annotations

import asyncio
import json
import logging
import re
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import TYPE_CHECKING

import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from src.client import client

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

logger = logging.getLogger("webui")
logging.basicConfig(level=logging.INFO)

WEBUI_DIR = Path(__file__).resolve().parent
INDEX_FILE = WEBUI_DIR / "index.html"
AGENT_NAME = "AgentLocalFiles"

# Local 8B model on CPU can take a few minutes per full run; the source citation
# markers look like "[source: restack_overview.md | score: 0.71]".
SOURCE_PATTERN = re.compile(r"\[source:\s*([^|\]]+?)\s*[|\]]")


class ChatRequest(BaseModel):
    message: str


class Session:
    """A single chat session backed by one long-lived agent run."""

    def __init__(self) -> None:
        self.agent_id: str | None = None
        self.run_id: str | None = None
        # Serialise access: the agent holds one conversation and each run can
        # take minutes, so requests must not interleave.
        self.lock = asyncio.Lock()


session = Session()


async def _start_run() -> None:
    agent_id = f"{int(time.time() * 1000)}-{AGENT_NAME}"
    run_id = await client.schedule_agent(agent_name=AGENT_NAME, agent_id=agent_id)
    session.agent_id = agent_id
    session.run_id = run_id
    logger.info("Started agent run agent_id=%s run_id=%s", agent_id, run_id)


async def _ensure_run() -> None:
    if not session.agent_id or not session.run_id:
        await _start_run()


def _strip_tool_syntax(text: str) -> str:
    """Remove any raw tool-call JSON the model may have leaked into an answer.

    Non-technical users should only ever see natural language, never a
    ``{"name": ..., "parameters": ...}`` blob or ``<tool_call>`` tag.
    """
    text = re.sub(r"<tool_call>.*?</tool_call>", "", text, flags=re.DOTALL)
    decoder = json.JSONDecoder()
    out: list[str] = []
    index = 0
    while index < len(text):
        if text[index] == "{":
            try:
                obj, end = decoder.raw_decode(text[index:])
            except ValueError:
                obj = None
            if isinstance(obj, dict) and "name" in obj and (
                "parameters" in obj or "arguments" in obj
            ):
                index += end
                continue
        out.append(text[index])
        index += 1
    return "".join(out).strip()


def _extract_reply(messages: list) -> tuple[str, list[str]]:
    """Pull the latest assistant answer and cited sources for the last turn."""
    last_user = -1
    for index, message in enumerate(messages):
        if isinstance(message, dict) and message.get("role") == "user":
            last_user = index

    turn = messages[last_user + 1 :] if last_user >= 0 else messages
    reply = ""
    sources: list[str] = []
    for message in turn:
        if not isinstance(message, dict):
            continue
        content = message.get("content") or ""
        if message.get("role") == "tool":
            sources.extend(SOURCE_PATTERN.findall(content))
        elif message.get("role") == "assistant" and content.strip():
            reply = _strip_tool_syntax(content)

    unique_sources = list(dict.fromkeys(source.strip() for source in sources))
    return reply, unique_sources


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    # Schedule the session's run up front so the first message is faster. If the
    # engine is not ready yet, defer to the first request instead of crashing.
    try:
        await _start_run()
    except Exception as error:  # noqa: BLE001 - startup should never hard-fail
        logger.warning("Could not start agent run on startup: %s", error)
    yield


app = FastAPI(title="Offline Local-Files Chat", lifespan=lifespan)


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(INDEX_FILE)


@app.post("/api/chat")
async def chat(request: ChatRequest) -> JSONResponse:
    message = (request.message or "").strip()
    if not message:
        return JSONResponse(
            status_code=400, content={"error": "Please type a message."}
        )
    try:
        async with session.lock:
            await _ensure_run()
            messages = await client.send_agent_event(
                agent_id=session.agent_id,
                run_id=session.run_id,
                event_name="messages",
                event_input={
                    "messages": [{"role": "user", "content": message}]
                },
                wait_for_completion=True,
            )
    except Exception as error:
        logger.exception("chat request failed")
        return JSONResponse(status_code=500, content={"error": str(error)})

    reply, sources = _extract_reply(messages or [])
    if not reply:
        reply = "Sorry, I couldn't produce an answer. Please try rephrasing."
    return JSONResponse(content={"reply": reply, "sources": sources})


@app.post("/api/new")
async def new_chat() -> JSONResponse:
    try:
        async with session.lock:
            await _start_run()
    except Exception as error:
        logger.exception("could not start a new chat")
        return JSONResponse(status_code=500, content={"error": str(error)})
    return JSONResponse(content={"ok": True})


def main() -> None:
    # Keep-alive is generous because a single answer can take a few minutes on
    # CPU-only local inference.
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8000,
        timeout_keep_alive=600,
    )


if __name__ == "__main__":
    main()
