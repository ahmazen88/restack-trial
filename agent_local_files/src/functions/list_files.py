from pydantic import BaseModel, Field
from restack_ai.function import NonRetryableError, function, log

from src.fileaccess import BASE_DIR, resolve_readable


class ListFilesInput(BaseModel):
    directory: str = Field(
        default="knowledge",
        description="Directory (relative to the project root) to list",
    )


class ListFilesOutput(BaseModel):
    files: list[str]


@function.defn()
async def list_files(function_input: ListFilesInput) -> ListFilesOutput:
    try:
        log.info("list_files started", function_input=function_input)
        target = resolve_readable(function_input.directory)
        if not target.exists():
            return ListFilesOutput(files=[])
        files = [
            str(path.relative_to(BASE_DIR))
            for path in sorted(target.rglob("*"))
            if path.is_file()
        ]
        return ListFilesOutput(files=files)
    except Exception as e:
        error_message = f"list_files failed: {e}"
        raise NonRetryableError(error_message) from e
