from backend.core.llm import get_llm
import os
from backend.core.embeddings import get_embedding_model
from langchain_community.vectorstores import FAISS

VECTOR_DB_DIR = "backend/vector_db"

class ResumeImprovementAgent:
    def __init__(self):
        self.embeddings = get_embedding_model()
        self.llm = get_llm()

    def run(self,resume_id: str,question:str,k:int = 4)->dict:

         """
         Analyse resume and suggest improvements
         """

         vector_store = FAISS.load_local(
              f"{VECTOR_DB_DIR}/{resume_id}",
              self.embeddings,
              allow_dangerous_deserialization = True
              
         )

         docs = vector_store.similarity_search(question, k = 8)

         if not docs:
            return "Resume not uploaded or no information found in resume "
        
         context = "\n\n".join(doc.page_content for doc in docs)

         prompt = f""" 
        You are a senior technical recruiter and resume reviewer.

Analyze the resume below and provide constructive feedback.

Resume Content:
{context}

Provide output in the following structure:

1. Overall Assessment (2-3 lines)
2. Strengths (bullet points)
3. Weaknesses / Gaps (bullet points)
4. Specific Improvements (bullet points)
5. Missing Sections (if any)

Be honest, actionable, and professional.
"""

         response = self.llm.invoke(prompt)

         return response.strip()
        
                      
