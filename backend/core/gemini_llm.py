# backend/core/gemini_llm.py
from google import genai
import os

class GeminiLLM:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

        self.model = "models/gemini-2.5-flash-lite"

    def invoke(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        return response.text
