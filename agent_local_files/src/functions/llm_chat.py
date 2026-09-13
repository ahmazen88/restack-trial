import os
from typing import Literal

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_message_tool_call import (
    ChatCompletionMessageToolCall,
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
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2")


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
        )

        log.info("llm_chat function completed", result=result)

        return result.model_dump()
    except Exception as e:
        error_message = f"LLM chat failed: {e}"
        raise NonRetryableError(error_message) from e
