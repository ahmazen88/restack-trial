from datetime import timedelta

from pydantic import BaseModel
from restack_ai.agent import NonRetryableError, agent, import_functions, log

with import_functions():
    from src.functions.llm_lmstudio import (
        LmStudioInput,
        Message,
        llm_lmstudio,
    )


class MessagesEvent(BaseModel):
    messages: list[Message]


class EndEvent(BaseModel):
    end: bool


class ConfigEvent(BaseModel):
    """Event to configure model parameters."""

    model: str | None = None
    temperature: float | None = None
    max_tokens: int | None = None
    system_content: str | None = None


@agent.defn()
class QwenAgent:
    """Agent using Qwen 2.5 7B Instruct via LM Studio.

    This agent connects to LM Studio's local OpenAI-compatible API
    to run Qwen 2.5 7B Instruct Q4_K_M quantized model.

    Default LM Studio endpoint: http://localhost:1234/v1
    """

    def __init__(self) -> None:
        self.end = False
        self.messages = []
        self.model = None
        self.temperature = 0.7
        self.max_tokens = 2048
        self.system_content = (
            "You are a helpful AI assistant powered by "
            "Qwen 2.5 7B running locally via LM Studio."
        )

    @agent.event
    async def configure(self, config: ConfigEvent) -> dict:
        """Configure model parameters dynamically."""
        log.info(f"Received configuration: {config}")
        if config.model:
            self.model = config.model
        if config.temperature is not None:
            self.temperature = config.temperature
        if config.max_tokens is not None:
            self.max_tokens = config.max_tokens
        if config.system_content is not None:
            self.system_content = config.system_content
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "system_content": self.system_content,
        }

    @agent.event
    async def messages(
        self, messages_event: MessagesEvent
    ) -> list[Message]:
        log.info(f"Received messages: {messages_event.messages}")
        self.messages.extend(messages_event.messages)

        log.info(
            f"Calling llm_lmstudio with messages: {self.messages}"
        )
        try:
            assistant_message = await agent.step(
                function=llm_lmstudio,
                function_input=LmStudioInput(
                    messages=self.messages,
                    model=self.model,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    system_content=self.system_content,
                ),
                start_to_close_timeout=timedelta(seconds=120),
            )
        except Exception as e:
            error_message = f"Error during llm_lmstudio: {e}"
            raise NonRetryableError(error_message) from e
        else:
            self.messages.append(assistant_message)
            return self.messages

    @agent.event
    async def end(self, end: EndEvent) -> EndEvent:
        log.info("Received end")
        self.end = True
        return end

    @agent.run
    async def run(self, function_input: dict) -> None:
        log.info(
            "QwenAgent function_input",
            function_input=function_input,
        )
        await agent.condition(lambda: self.end)


# Alias for convenience
qwen_agent = QwenAgent
