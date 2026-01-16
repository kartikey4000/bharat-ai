from backend.resume_ingestion.query import query_resume
import os
from backend.core.llm import get_llm


class InterviewerAgent:
    """
    Simulates a real interviewer evaluating a resume.

    """

    def evaluate(self,resume_id:str,role:str)->dict:
        resume_chunks = query_resume(
              resume_id = resume_id,
              query = f"skills, projects, experience relevant to {role}",
              k = 5

        )

        context = "/n".join(resume_chunks)

        prompt = f"""
You are a professional technical interviewer.

Evaluate the following resume for the role: {role}

Resume Context:
{context}

Respond in the following format:

Decision: Yes / No / Maybe
Strengths:
- ...
Concerns:
- ...
Skill Gaps:
- ...
Interview Questions:
- ...
"""

       
        llm = get_llm()
        response = llm.invoke(prompt).strip()

        return  response
        