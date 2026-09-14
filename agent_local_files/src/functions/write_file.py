from pydantic import BaseModel, Field
from restack_ai.function import NonRetryableError, function, log

from src.fileaccess import BASE_DIR, resolve_writable


class WriteFileInput(BaseModel):
    path: str = Field(
        description="File to write, relative to the 'workspace/' directory, e.g. 'summary.md'"
    )
    content: str = Field(description="The text content to write to the file")


class WriteFileOutput(BaseModel):
    path: str
    bytes_written: int


@function.defn()
async def write_file(function_input: WriteFileInput) -> WriteFileOutput:
    try:
        log.info("write_file started", path=function_input.path)
        target = resolve_writable(function_input.path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(function_input.content, encoding="utf-8")
        return WriteFileOutput(
            path=str(target.relative_to(BASE_DIR)),
            bytes_written=len(function_input.content.encode("utf-8")),
        )
    except Exception as e:
        error_message = f"write_file failed: {e}"
        raise NonRetryableError(error_message) from e
