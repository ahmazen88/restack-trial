from datetime import timedelta

from pydantic import BaseModel
from restack_ai.agent import (
    NonRetryableError,
    agent,
    import_functions,
    log,
)

with import_functions():
    from openai import pydantic_function_tool

    from src.functions.list_files import (
        ListFilesInput,
        list_files,
    )
    from src.functions.llm_chat import (
        LlmChatInput,
        Message,
        llm_chat,
    )
    from src.functions.read_file import ReadFileInput, read_file
    from src.functions.search_knowledge import (
        SearchKnowledgeInput,
        search_knowledge,
    )
    from src.functions.write_file import (
        WriteFileInput,
        write_file,
    )

MAX_TOOL_ITERATIONS = 6
# Generous timeout: the local 8B model runs on CPU, so a single chat completion
# that also generates the file content can take well over a minute.
STEP_TIMEOUT = timedelta(seconds=240)

SYSTEM_PROMPT = (
    "You are a friendly, fully offline assistant that answers questions using "
    "the user's local files, all with local models. To answer a question, "
    "first call the search_knowledge tool with a `query` describing what to "
    "look up in the local knowledge base. Use list_files to discover files, "
    "read_file only to read a specific file the user names, and write_file to "
    "save a file into the local 'workspace/' folder when asked. Do not guess "
    "file names. Ground every answer in the tool results and cite the source "
    "files you used. Always reply to the user in clear, friendly, plain "
    "sentences — never output tool calls, JSON, or function syntax as your "
    "answer. Keep answers concise: a short, direct paragraph is best; only add "
    "more when the question truly needs it."
)


class MessagesEvent(BaseModel):
    messages: list[Message]


class EndEvent(BaseModel):
    end: bool


def _build_tools() -> list:
    return [
        pydantic_function_tool(
            model=SearchKnowledgeInput,
            name="search_knowledge",
            description="Semantic search over the local knowledge base (RAG)",
        ),
        pydantic_function_tool(
            model=ListFilesInput,
            name="list_files",
            description="List files in a local directory under the project root",
        ),
        pydantic_function_tool(
            model=ReadFileInput,
            name="read_file",
            description="Read the contents of a local file under the project root",
        ),
        pydantic_function_tool(
            model=WriteFileInput,
            name="write_file",
            description="Write text to a file in the local 'workspace/' folder",
        ),
    ]


@agent.defn()
class AgentLocalFiles:
    def __init__(self) -> None:
        self.end = False
        self.messages = [Message(role="system", content=SYSTEM_PROMPT)]

    async def _run_tool(self, name: str, arguments: str) -> str:
        if name == "search_knowledge":
            output = await agent.step(
                function=search_knowledge,
                function_input=SearchKnowledgeInput.model_validate_json(arguments),
                start_to_close_timeout=STEP_TIMEOUT,
            )
            return output.results
        if name == "list_files":
            output = await agent.step(
                function=list_files,
                function_input=ListFilesInput.model_validate_json(arguments),
                start_to_close_timeout=STEP_TIMEOUT,
            )
            return "\n".join(output.files) or "(no files)"
        if name == "read_file":
            output = await agent.step(
                function=read_file,
                function_input=ReadFileInput.model_validate_json(arguments),
                start_to_close_timeout=STEP_TIMEOUT,
            )
            return output.content
        if name == "write_file":
            output = await agent.step(
                function=write_file,
                function_input=WriteFileInput.model_validate_json(arguments),
                start_to_close_timeout=STEP_TIMEOUT,
            )
            return f"Wrote {output.bytes_written} bytes to {output.path}"
        return f"Unknown tool: {name}"

    @agent.event
    async def messages(self, messages_event: MessagesEvent) -> list[Message]:
        log.info(f"Received messages: {messages_event.messages}")
        self.messages.extend(messages_event.messages)

        tools = _build_tools()
        answered = False

        for _ in range(MAX_TOOL_ITERATIONS):
            try:
                completion = await agent.step(
                    function=llm_chat,
                    function_input=LlmChatInput(
                        messages=self.messages, tools=tools
                    ),
                    start_to_close_timeout=STEP_TIMEOUT,
                )
            except Exception as e:
                error_message = f"Error during llm_chat: {e}"
                raise NonRetryableError(error_message) from e

            message = completion.choices[0].message
            tool_calls = message.tool_calls
            self.messages.append(
                Message(
                    role="assistant",
                    content=message.content or "",
                    tool_calls=tool_calls,
                )
            )

            if not tool_calls:
                answered = True
                break

            for tool_call in tool_calls:
                log.info(f"tool_call: {tool_call.function.name}")
                try:
                    result = await self._run_tool(
                        tool_call.function.name,
                        tool_call.function.arguments,
                    )
                except Exception as e:  # noqa: BLE001
                    # Feed tool errors (e.g. reading a file that does not exist)
                    # back to the model so it can recover instead of crashing
                    # the whole chat turn.
                    log.warning(f"tool {tool_call.function.name} failed: {e}")
                    result = (
                        f"Error running {tool_call.function.name}: {e}. "
                        "Try a different tool such as search_knowledge or "
                        "list_files."
                    )
                self.messages.append(
                    Message(
                        role="tool",
                        tool_call_id=tool_call.id,
                        content=str(result),
                    )
                )

        if not answered:
            # Force a final natural-language answer without further tool calls.
            completion = await agent.step(
                function=llm_chat,
                function_input=LlmChatInput(messages=self.messages),
                start_to_close_timeout=STEP_TIMEOUT,
            )
            self.messages.append(
                Message(
                    role="assistant",
                    content=completion.choices[0].message.content or "",
                )
            )

        return self.messages

    @agent.event
    async def end(self) -> EndEvent:
        log.info("Received end")
        self.end = True
        return {"end": True}

    @agent.run
    async def run(self, agent_input: dict) -> None:
        log.info("AgentLocalFiles agent_input", agent_input=agent_input)
        await agent.condition(lambda: self.end)
