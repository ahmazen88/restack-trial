"""A tiny, fully-offline vector index over local files.

Text files under ``knowledge/`` are chunked, embedded with a local Ollama
embedding model (``nomic-embed-text``) through the OpenAI-compatible API, and
stored on disk as an embeddings matrix plus JSON metadata. Retrieval embeds the
query and ranks chunks by cosine similarity. No data leaves the machine.
"""

from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import numpy as np
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = Path(
    os.environ.get("KNOWLEDGE_DIR", str(BASE_DIR / "knowledge"))
)
INDEX_DIR = BASE_DIR / ".index"
META_FILE = INDEX_DIR / "index.json"
EMB_FILE = INDEX_DIR / "embeddings.npy"

OLLAMA_BASE_URL = os.environ.get(
    "OLLAMA_BASE_URL", "http://localhost:11434/v1"
)
EMBED_MODEL = os.environ.get("OLLAMA_EMBED_MODEL", "nomic-embed-text")

TEXT_SUFFIXES = {".md", ".txt", ".rst", ".py", ".json", ".yaml", ".yml"}
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150


def _client() -> OpenAI:
    # api_key is required by the client but ignored by Ollama.
    return OpenAI(
        base_url=OLLAMA_BASE_URL,
        api_key=os.environ.get("OLLAMA_API_KEY", "ollama"),
    )


def _embed(texts: list[str]) -> np.ndarray:
    response = _client().embeddings.create(model=EMBED_MODEL, input=texts)
    vectors = np.array([item.embedding for item in response.data], dtype=np.float32)
    # Normalise so that a dot product equals cosine similarity.
    norms = np.linalg.norm(vectors, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return vectors / norms


def _chunk(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = start + CHUNK_SIZE
        chunks.append(text[start:end])
        start = end - CHUNK_OVERLAP
    return chunks


def _iter_files() -> list[Path]:
    if not KNOWLEDGE_DIR.exists():
        return []
    return sorted(
        path
        for path in KNOWLEDGE_DIR.rglob("*")
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES
    )


def _fingerprint(files: list[Path]) -> str:
    hasher = hashlib.sha256()
    for path in files:
        stat = path.stat()
        hasher.update(str(path).encode())
        hasher.update(str(stat.st_size).encode())
        hasher.update(str(int(stat.st_mtime)).encode())
    return hasher.hexdigest()


def build_index() -> dict:
    """Read files, embed their chunks, and persist the index. Idempotent."""
    files = _iter_files()
    records: list[dict] = []
    texts: list[str] = []
    for path in files:
        content = path.read_text(encoding="utf-8", errors="ignore")
        for position, chunk in enumerate(_chunk(content)):
            records.append(
                {
                    "id": f"{path.name}:{position}",
                    "source": str(path.relative_to(KNOWLEDGE_DIR)),
                    "text": chunk,
                }
            )
            texts.append(chunk)

    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    embeddings = (
        _embed(texts)
        if texts
        else np.zeros((0, 1), dtype=np.float32)
    )
    np.save(EMB_FILE, embeddings)
    meta = {"fingerprint": _fingerprint(files), "records": records}
    META_FILE.write_text(json.dumps(meta), encoding="utf-8")
    return meta


def ensure_index() -> dict:
    """Build the index on first use or whenever the source files change."""
    files = _iter_files()
    if META_FILE.exists() and EMB_FILE.exists():
        meta = json.loads(META_FILE.read_text(encoding="utf-8"))
        if meta.get("fingerprint") == _fingerprint(files):
            return meta
    return build_index()


def search(query: str, k: int = 4) -> list[dict]:
    """Return the ``k`` most similar chunks to ``query`` with source + score."""
    meta = ensure_index()
    records = meta.get("records", [])
    if not records:
        return []
    embeddings = np.load(EMB_FILE)
    query_vector = _embed([query])[0]
    scores = embeddings @ query_vector
    top = np.argsort(scores)[::-1][:k]
    return [
        {
            "source": records[i]["source"],
            "text": records[i]["text"],
            "score": float(scores[i]),
        }
        for i in top
    ]
