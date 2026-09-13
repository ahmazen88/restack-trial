"""Build (or rebuild) the local vector index from files under knowledge/.

Run with `uv run ingest`. This is optional: the agent also builds the index
automatically on first search and whenever the source files change.
"""

from src.knowledge_base import KNOWLEDGE_DIR, build_index


def run_ingest() -> None:
    meta = build_index()
    count = len(meta.get("records", []))
    print(  # noqa: T201
        f"Indexed {count} chunks from files under {KNOWLEDGE_DIR}"
    )


if __name__ == "__main__":
    run_ingest()
