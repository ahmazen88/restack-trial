import json
import os
import re
from typing import Literal

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_message_tool_call import (
    ChatCompletionMessageToolCall,
    Function,
)
from openai.types.chat.chat_completion_tool_param import (
    ChatCompletionToolParam,
)
from pydantic import BaseModel
from restack_ai.function import NonRetryableError, function, log

load_dotenv()

# Fully offline LLM: talk to a local Ollama server through its
# OpenAI-compatible endpoint. No external API and no API key required.
OLLAMA_BASE_URL = os.environ.get(
    "OLLAMA_BASE_URL", "http://localhost:11434/v1"
)
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.1:8b")
# Low temperature keeps local tool-calling deterministic and reliable.
OLLAMA_TEMPERATURE = float(os.environ.get("OLLAMA_TEMPERATURE", "0"))


class Message(BaseModel):
    role: Literal["system", "user", "assistant", "tool"]
    content: str
    tool_call_id: str | None = None
    tool_calls: list[ChatCompletionMessageToolCall] | None = None


class LlmChatInput(BaseModel):
    system_content: str | None = None
    model: str | None = None
    messages: list[Message] | None = None
    tools: list[ChatCompletionToolParam] | None = None


def raise_exception(message: str) -> None:
    log.error(message)
    raise NonRetryableError(message)


def _allowed_tool_names(tools: list | None) -> set[str]:
    names: set[str] = set()
    for tool in tools or []:
        fn = tool.get("function") if isinstance(tool, dict) else getattr(tool, "function", None)
        name = fn.get("name") if isinstance(fn, dict) else getattr(fn, "name", None)
        if name:
            names.add(name)
    return names


def _recover_tool_calls_from_text(
    content: str | None, allowed: set[str]
) -> list[ChatCompletionMessageToolCall] | None:
    """Recover a tool call that the model emitted as plain text.

    Some local models (e.g. qwen2.5 served by Ollama) occasionally return a tool
    call as JSON in the message content instead of a structured ``tool_calls``
    entry, so Ollama never parses it. The model still genuinely decided to call
    the tool with valid arguments, so we normalise that JSON back into a real
    tool call rather than losing the intent.
    """
    if not content:
        return None
    text = content.strip()
    if text.startswith("```"):
        text = re.sub(r"^```[a-zA-Z]*\n?", "", text).rstrip("`").strip()
    tag = re.search(r"<tool_call>\s*(.+?)\s*</tool_call>", text, re.DOTALL)
    if tag:
        text = tag.group(1).strip()
    if not text.startswith(("{", "[")):
        return None
    try:
        data = json.loads(text)
    except (ValueError, TypeError):
        return None
    items = data if isinstance(data, list) else [data]
    recovered: list[ChatCompletionMessageToolCall] = []
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        arguments = item.get("arguments", item.get("parameters"))
        if name not in allowed or not isinstance(arguments, dict | str):
            continue
        arguments_json = (
            arguments if isinstance(arguments, str) else json.dumps(arguments)
        )
        recovered.append(
            ChatCompletionMessageToolCall(
                id=f"call_recovered_{index}",
                type="function",
                function=Function(name=name, arguments=arguments_json),
            )
        )
    return recovered or None


@function.defn()
async def llm_chat(function_input: LlmChatInput) -> ChatCompletion:
    try:
        log.info("llm_chat function started", function_input=function_input)

        # api_key is required by the OpenAI client but ignored by Ollama.
        client = OpenAI(
            base_url=OLLAMA_BASE_URL,
            api_key=os.environ.get("OLLAMA_API_KEY", "ollama"),
        )

        log.info("pydantic_function_tool", tools=function_input.tools)

        if function_input.system_content:
            function_input.messages.append(
                Message(
                    role="system",
                    content=function_input.system_content or "",
                )
            )

        result = client.chat.completions.create(
            model=function_input.model or OLLAMA_MODEL,
            messages=function_input.messages,
            tools=function_input.tools,
            temperature=OLLAMA_TEMPERATURE,
        )

        message = result.choices[0].message
        if not message.tool_calls:
            recovered = _recover_tool_calls_from_text(
                message.content, _allowed_tool_names(function_input.tools)
            )
            if recovered:
                log.info("recovered tool calls from text content", tool_calls=recovered)
                message.tool_calls = recovered
                message.content = None

        log.info("llm_chat function completed", result=result)

        return result.model_dump()
    except Exception as e:
        error_message = f"LLM chat failed: {e}"
        raise NonRetryableError(error_message) from e
