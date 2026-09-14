from pydantic import BaseModel, Field
from restack_ai.function import NonRetryableError, function, log

from src.knowledge_base import search

# Clamp how many chunks we retrieve so the answer stays grounded even when a
# small local model asks for too few (e.g. k=0 or k=1) or too many chunks.
MIN_K = 3
MAX_K = 8


class SearchKnowledgeInput(BaseModel):
    query: str = Field(description="What to look up in the local knowledge base")
    k: int = Field(default=4, description="How many chunks to return")


class SearchKnowledgeOutput(BaseModel):
    results: str


@function.defn()
async def search_knowledge(
    function_input: SearchKnowledgeInput,
) -> SearchKnowledgeOutput:
    try:
        log.info("search_knowledge started", function_input=function_input)
        k = max(MIN_K, min(function_input.k, MAX_K))
        hits = search(function_input.query, k=k)
        if not hits:
            return SearchKnowledgeOutput(
                results="No matching content found in the local knowledge base."
            )
        formatted = "\n\n".join(
            f"[source: {hit['source']} | score: {hit['score']:.3f}]\n{hit['text']}"
            for hit in hits
        )
        return SearchKnowledgeOutput(results=formatted)
    except Exception as e:
        error_message = f"search_knowledge failed: {e}"
        raise NonRetryableError(error_message) from e
