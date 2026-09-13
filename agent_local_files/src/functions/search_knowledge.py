from pydantic import BaseModel, Field
from restack_ai.function import NonRetryableError, function, log

from src.knowledge_base import search


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
        hits = search(function_input.query, k=function_input.k)
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
