"""Path sandboxing helpers.

Reads and listings are confined to the example root; writes are confined to the
``workspace/`` sub-directory. This keeps the agent's file access local and safe.
"""

from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
WORKSPACE_DIR = BASE_DIR / "workspace"


def _resolve_within(base: Path, relative: str) -> Path:
    candidate = (base / relative).resolve()
    base = base.resolve()
    if base != candidate and base not in candidate.parents:
        message = f"Path '{relative}' is outside the allowed directory"
        raise ValueError(message)
    return candidate


def resolve_readable(relative: str) -> Path:
    return _resolve_within(BASE_DIR, relative)


def resolve_writable(relative: str) -> Path:
    return _resolve_within(WORKSPACE_DIR, relative)
