from pydantic import BaseModel, Field
from restack_ai.function import NonRetryableError, function, log

from src.fileaccess import resolve_readable

MAX_CHARS = 8000


class ReadFileInput(BaseModel):
    path: str = Field(
        description="File path relative to the project root, e.g. 'knowledge/restack_overview.md'"
    )


class ReadFileOutput(BaseModel):
    path: str
    content: str


@function.defn()
async def read_file(function_input: ReadFileInput) -> ReadFileOutput:
    log.info("read_file started", function_input=function_input)
    target = resolve_readable(function_input.path)
    if not target.is_file():
        message = f"File not found: {function_input.path}"
        raise NonRetryableError(message)
    try:
        content = target.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        error_message = f"read_file failed: {e}"
        raise NonRetryableError(error_message) from e
    return ReadFileOutput(path=function_input.path, content=content[:MAX_CHARS])
