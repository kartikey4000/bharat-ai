from backend.core.llm import get_llm
import os
from backend.core.embeddings import get_embedding_model
from langchain_community.vectorstores import FAISS

VECTOR_DB_DIR = "backend/vector_db"

class ResumeComparisonAgent:
    def __init__(self):
        self.embeddings = get_embedding_model()
        self.llm = get_llm()

    def run(self,resume_id_a:str,resume_id_b:str,role: str|None)->str:
         """
        Compare two resumes for a given role.
         """
         vs_a = FAISS.load_local(
            f"{VECTOR_DB_DIR}/{resume_id_a}",
            self.embeddings,
            allow_dangerous_deserialization=True
        )

         vs_b = FAISS.load_local(
            f"{VECTOR_DB_DIR}/{resume_id_b}",
            self.embeddings,
            allow_dangerous_deserialization=True
        )

         docs_a = vs_a.similarity_search(role, k=6)
         docs_b = vs_b.similarity_search(role, k=6)

         context_a = "\n\n".join(doc.page_content for doc in docs_a)
         context_b = "\n\n".join(doc.page_content for doc in docs_b)

       
         prompt = f"""
You are a senior technical recruiter.

Compare the following two resumes for the role of {role}.

Resume A:
{context_a}

Resume B:
{context_b}

Provide comparison in the following structure:

1. Candidate A – Strengths
2. Candidate A – Weaknesses
3. Candidate B – Strengths
4. Candidate B – Weaknesses
5. Final Recommendation (Who should be shortlisted and why)

Be fair, concise, and role-focused.
"""

      
         response = self.llm.invoke(prompt)

         return  response.strip()
        