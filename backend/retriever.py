from logger import setup_logger
from vector_store import get_vector_store

logger = setup_logger()


def retrieve_context(query: str, k: int = 3) -> str:
    logger.info(f"Retrieving context for query: {query}")

    vector_store = get_vector_store()

    docs = vector_store.similarity_search(query, k=k)

    if not docs:
        logger.warning("No relevant documents found")
        return "No relevant context found."

    context_parts = []

    for i, doc in enumerate(docs, start=1):
        source = doc.metadata.get("source", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")

        context_parts.append(
            f"[Document {i} | Source: {source} | Chunk: {chunk_id}]\n"
            f"{doc.page_content}"
        )

    logger.info(f"Retrieved {len(docs)} documents")

    return "\n\n".join(context_parts)
