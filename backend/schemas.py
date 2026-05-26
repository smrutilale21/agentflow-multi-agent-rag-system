from typing import List

from pydantic import BaseModel, Field


class ResearchResult(BaseModel):
    research_notes: str = Field(description="Brief notes based on retrieved context")
    final_answer: str = Field(description="Final answer grounded in retrieved context")
    sources: List[str] = Field(description="Sources or chunk references used")
    confidence: str = Field(description="Confidence level: Low, Medium, or High")
