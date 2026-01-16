# backend/core/llm.py
import os
from backend.core.gemini_llm import GeminiLLM

def get_llm():
    """
    Central LLM factory.
    Switch providers here without touching agents.
    """
    provider = os.getenv("LLM_PROVIDER", "gemini")

    if provider == "gemini":
        return GeminiLLM()

    raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")
