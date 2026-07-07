import os
from typing import Literal

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from restack_ai.function import NonRetryableError, function, log

load_dotenv()

# LM Studio default configuration
LM_STUDIO_BASE_URL = os.environ.get(
    "LM_STUDIO_BASE_URL", "http://localhost:1234/v1"
)
# Qwen 2.5 7B Instruct Q4_K_M model identifier in LM Studio
LM_STUDIO_MODEL = os.environ.get(
    "LM_STUDIO_MODEL",
    "qwen2.5-7b-instruct-q4_k_m",
)


class Message(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str


class LmStudioInput(BaseModel):
    system_content: str | None = None
    model: str | None = None
    messages: list[Message] | None = None
    temperature: float | None = 0.7
    max_tokens: int | None = 2048


def raise_exception(message: str) -> None:
    log.error(message)
    raise NonRetryableError(message)


@function.defn()
async def llm_lmstudio(
    agent_input: LmStudioInput,
) -> dict[str, str]:
    """Call Qwen 2.5 7B model via LM Studio's OpenAI-compatible API.

    LM Studio runs a local server that provides an OpenAI-compatible
    API endpoint. By default, it runs on http://localhost:1234/v1.

    Args:
        agent_input: Input containing messages and optional parameters.

    Returns:
        Dictionary with role and content of assistant response.
    """
    try:
        log.info(
            "llm_lmstudio function started",
            agent_input=agent_input,
        )

        # LM Studio doesn't require an API key, but OpenAI client
        # needs a placeholder value
        client = OpenAI(
            base_url=LM_STUDIO_BASE_URL,
            api_key="lm-studio",  # Placeholder, not validated
        )

        messages = list(agent_input.messages) if agent_input.messages else []

        if agent_input.system_content:
            messages.insert(
                0,
                {"role": "system", "content": agent_input.system_content},
            )

        model = agent_input.model or LM_STUDIO_MODEL

        log.info(
            "Calling LM Studio",
            model=model,
            base_url=LM_STUDIO_BASE_URL,
            num_messages=len(messages),
        )

        assistant_raw_response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=agent_input.temperature,
            max_tokens=agent_input.max_tokens,
        )

    except Exception as e:
        error_message = f"LM Studio chat failed: {e}"
        raise NonRetryableError(error_message) from e
    else:
        log.info(
            "llm_lmstudio function completed",
            assistant_raw_response=assistant_raw_response,
        )

        assistant_response = {
            "role": assistant_raw_response.choices[0].message.role,
            "content": assistant_raw_response.choices[0].message.content,
        }

        log.info(
            "assistant_response",
            assistant_response=assistant_response,
        )

        return assistant_response
