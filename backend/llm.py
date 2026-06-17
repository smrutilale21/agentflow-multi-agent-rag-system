import os
from config import get_openai_api_key
from langchain_openai import ChatOpenAI


def get_llm() -> ChatOpenAI:
    api_key = get_openai_api_key()

    return ChatOpenAI(
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        temperature=0,
        api_key=api_key,
    )
