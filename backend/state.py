from typing import List, TypedDict


class ResearchState(TypedDict):
    user_query: str
    refined_query: str
    retrieved_context: str
    research_notes: str
    sources: List[str]
    final_answer: str
    confidence: str
