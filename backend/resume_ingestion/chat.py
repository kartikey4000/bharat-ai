from backend.resume_ingestion.query import query_resume
import os
from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from backend.core.llm import get_llm
from backend.agents.base_agent import BaseAgent

baseagent = BaseAgent()


class ChatRequest(BaseModel):
    question: str
    role: str
    resume_id: str | None = None
    compare_resume_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[str] | None = None


router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest):

    result = baseagent.handle_request(
        question=request.question,
        resume_id=request.resume_id,
        role=request.role,
        compare_resume_id=request.compare_resume_id
    )

    return {
        "answer": result["answer"],
        "sources": None
    }




    
        


