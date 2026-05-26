from llm import get_llm
from logger import setup_logger
from prompts import PLANNER_PROMPT, RAG_RESEARCH_PROMPT, RETRY_RAG_RESEARCH_PROMPT
from retriever import retrieve_context
from schemas import ResearchResult
from state import ResearchState
from utils import clean_json_response, safe_parse_json

logger = setup_logger()
llm = get_llm()


def planner_node(state: ResearchState) -> dict:
    logger.info("Planner node started")

    user_query = state["user_query"]

    prompt = PLANNER_PROMPT.format(user_query=user_query)
    response = llm.invoke(prompt)

    refined_query = response.content.strip()

    logger.info(f"Refined query: {refined_query}")

    return {"refined_query": refined_query}


def retriever_node(state: ResearchState) -> dict:
    logger.info("Retriever node started")

    refined_query = state["refined_query"]
    retrieved_context = retrieve_context(refined_query, k=3)

    return {"retrieved_context": retrieved_context}


def research_node(state: ResearchState) -> dict:
    logger.info("Research node started")

    refined_query = state["refined_query"]
    retrieved_context = state["retrieved_context"]

    prompt = RAG_RESEARCH_PROMPT.format(
        refined_query=refined_query, retrieved_context=retrieved_context
    )

    try:
        response = llm.invoke(prompt)
        raw_output = response.content

        try:
            cleaned = clean_json_response(raw_output)
            parsed = safe_parse_json(cleaned)

        except Exception:
            logger.warning(
                "Initial JSON parsing failed. Retrying with stricter prompt."
            )

            retry_prompt = RETRY_RAG_RESEARCH_PROMPT.format(
                bad_output=raw_output,
                refined_query=refined_query,
                retrieved_context=retrieved_context,
            )

            retry_response = llm.invoke(retry_prompt)
            cleaned = clean_json_response(retry_response.content)
            parsed = safe_parse_json(cleaned)

        result = ResearchResult(**parsed)

        logger.info("Research result validated successfully")

        return {
            "research_notes": result.research_notes,
            "final_answer": result.final_answer,
            "sources": "\n".join(result.sources),
            "confidence": result.confidence,
        }

    except Exception as e:
        logger.error(f"Research node failed: {e}")

        return {
            "research_notes": "Research failed due to an internal error.",
            "final_answer": f"Something went wrong while generating the answer: {e}",
            "sources": "No sources available.",
            "confidence": "Low",
        }
