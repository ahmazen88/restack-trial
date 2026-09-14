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
# Cap generated tokens to shave CPU generation time. 512 is enough for a
# concise grounded answer or a short summary file without truncating, and can
# be raised via the environment when longer output is genuinely needed.
OLLAMA_MAX_TOKENS = int(os.environ.get("OLLAMA_MAX_TOKENS", "512"))


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


def _iter_json_objects(text: str) -> list:
    """Return JSON values found in ``text`` (pure JSON or embedded in prose)."""
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```[a-zA-Z]*\n?", "", stripped).rstrip("`").strip()
    tag = re.search(r"<tool_call>\s*(.+?)\s*</tool_call>", stripped, re.DOTALL)
    if tag:
        stripped = tag.group(1).strip()
    try:
        return [json.loads(stripped)]
    except (ValueError, TypeError):
        pass
    # Fall back to scanning for embedded objects (e.g. the model wrote prose and
    # then a raw {"name": ..., "parameters": ...} tool call).
    decoder = json.JSONDecoder()
    objects: list = []
    index = 0
    while index < len(stripped):
        if stripped[index] == "{":
            try:
                obj, end = decoder.raw_decode(stripped[index:])
                objects.append(obj)
                index += end
                continue
            except ValueError:
                pass
        index += 1
    return objects


# Small models sometimes use short/alternate argument names when they emit a
# tool call as text; map those back to the real parameter names.
_ARG_ALIASES: dict[str, dict[str, str]] = {
    "search_knowledge": {"q": "query", "search": "query", "text": "query"},
}


def _normalize_args(name: str, args: dict) -> dict:
    normalized = dict(args)
    for alias, canonical in _ARG_ALIASES.get(name, {}).items():
        if alias in normalized and canonical not in normalized:
            normalized[canonical] = normalized.pop(alias)
    return normalized


def _make_tool_call(index: int, name: str, arguments: str) -> ChatCompletionMessageToolCall:
    return ChatCompletionMessageToolCall(
        id=f"call_recovered_{index}",
        type="function",
        function=Function(name=name, arguments=arguments),
    )


# String argument fields to pull out per tool when the JSON is too malformed to
# parse. write_file's content can be huge/quoted, so it is matched last/greedily.
_STRING_FIELDS: dict[str, tuple[str, ...]] = {
    "search_knowledge": ("query",),
    "read_file": ("path",),
    "list_files": ("directory",),
    "write_file": ("path", "content"),
}


def _regex_recover(
    content: str, allowed: set[str]
) -> list[ChatCompletionMessageToolCall]:
    """Best-effort recovery when the emitted tool call JSON is malformed."""
    recovered: list[ChatCompletionMessageToolCall] = []
    for index, match in enumerate(
        re.finditer(r'"name"\s*:\s*"([a-zA-Z_]+)"', content)
    ):
        name = match.group(1)
        if name not in allowed:
            continue
        segment = content[match.end() :]
        args: dict[str, str] = {}
        for field in _STRING_FIELDS.get(name, ()):
            field_match = re.search(
                rf'"{field}"\s*:\s*"((?:[^"\\]|\\.)*)"', segment
            )
            if field_match:
                args[field] = (
                    field_match.group(1)
                    .replace('\\"', '"')
                    .replace("\\n", "\n")
                )
        if args:
            recovered.append(_make_tool_call(index, name, json.dumps(args)))
    return recovered


def _recover_tool_calls_from_text(
    content: str | None, allowed: set[str]
) -> list[ChatCompletionMessageToolCall] | None:
    """Recover a tool call that the model emitted as text instead of a real one.

    Local models served by Ollama (e.g. llama3.1 / qwen2.5) sometimes return a
    tool call as JSON in the message content — either as the whole message,
    embedded in a sentence, or as slightly malformed JSON — so Ollama never
    parses it into ``tool_calls``. The model still genuinely decided to call the
    tool, so we normalise that back into a real tool call rather than losing it.
    """
    if not content:
        return None
    recovered: list[ChatCompletionMessageToolCall] = []
    candidates: list = []
    for value in _iter_json_objects(content):
        candidates.extend(value if isinstance(value, list) else [value])
    for index, item in enumerate(candidates):
        if not isinstance(item, dict):
            continue
        name = item.get("name")
        arguments = item.get("arguments", item.get("parameters"))
        if name not in allowed or not isinstance(arguments, dict | str):
            continue
        if isinstance(arguments, dict):
            arguments = _normalize_args(name, arguments)
        arguments_json = (
            arguments if isinstance(arguments, str) else json.dumps(arguments)
        )
        recovered.append(_make_tool_call(index, name, arguments_json))
    if not recovered and '"name"' in content:
        recovered = _regex_recover(content, allowed)
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
            max_tokens=OLLAMA_MAX_TOKENS,
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
