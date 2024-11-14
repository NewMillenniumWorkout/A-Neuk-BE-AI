from langchain_openai import ChatOpenAI
from typing import List


async def remake_sentence(origin: str, emotions: List[str]) -> str:
    return f"{origin} remade by {emotions}"
