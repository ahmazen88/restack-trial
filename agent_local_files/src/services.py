import asyncio
import logging
import webbrowser
from pathlib import Path

from watchfiles import run_process

from src.agents.agent_local_files import AgentLocalFiles
from src.client import client
from src.functions.list_files import list_files
from src.functions.llm_chat import llm_chat
from src.functions.read_file import read_file
from src.functions.search_knowledge import search_knowledge
from src.functions.write_file import write_file


async def main() -> None:
    await client.start_service(
        agents=[AgentLocalFiles],
        functions=[
            llm_chat,
            search_knowledge,
            list_files,
            read_file,
            write_file,
        ],
    )


def run_services() -> None:
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Service interrupted by user. Exiting gracefully.")


def watch_services() -> None:
    watch_path = Path.cwd()
    logging.info("Watching %s and its subdirectories for changes...", watch_path)
    webbrowser.open("http://localhost:5233")
    run_process(watch_path, recursive=True, target=run_services)


if __name__ == "__main__":
    run_services()
