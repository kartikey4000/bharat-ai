from backend.resume_ingestion.query import query_resume
from backend.core.llm import get_llm

class ResumeScoringAgent:
    """
    Scores a resume like an ATS + recruiter.
    """

    def score(self, resume_id: str, role: str) -> dict:
        
        resume_chunks = query_resume(
            resume_id=resume_id,
            query=f"Skills, experience, projects relevant to {role}",
            k=6
        )

        context = "\n".join(resume_chunks)

       
        prompt = f"""
You are an Applicant Tracking System (ATS).

Evaluate the following resume for the role: {role}

Resume Context:
{context}

Give a STRICT evaluation in the following JSON format:

{{
  "ats_score": number between 0 and 100,
  "strengths": [list of strong points],
  "weaknesses": [list of weaknesses],
  "missing_skills": [important missing skills],
  "improvement_suggestions": [clear actionable suggestions],
  "verdict": "Strong Match / Moderate Match / Weak Match"
}}

Be realistic and professional.
"""

       
        llm = get_llm()
        response = llm.invoke(prompt)

        return response.strip();
