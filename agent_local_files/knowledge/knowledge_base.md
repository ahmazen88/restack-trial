# How the local knowledge base works

The agent answers questions using retrieval-augmented generation (RAG) over
files stored on disk, entirely offline.

Ingestion:

1. Every text file under the `knowledge/` directory is read from disk.
2. Each file is split into overlapping chunks of roughly 800 characters.
3. Each chunk is embedded with the local `nomic-embed-text` model.
4. The vectors and their source text are stored in a local index under
   `.index/` (an embeddings matrix plus a JSON metadata file).

The index is rebuilt automatically whenever the files in `knowledge/` change,
detected via a fingerprint of file names, sizes, and modification times.

Retrieval:

1. The user's query is embedded with the same model.
2. Cosine similarity is computed against every stored chunk.
3. The most similar chunks are returned to the model as grounding context,
   together with the name of the source file they came from.

Because retrieval always cites the source file, answers can be traced back to
the exact document on disk.
