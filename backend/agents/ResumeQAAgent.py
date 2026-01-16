from backend.core.llm import get_llm
import os
from backend.core.embeddings import get_embedding_model
from langchain_community.vectorstores import FAISS

VECTOR_DB_DIR = "backend/vector_db"

class ResumeQAAgent:
    def __init__(self):
        self.embeddings = get_embedding_model()
        self.llm = get_llm()

    def run(self,resume_id: str,question:str,k:int = 4)->str:

         """
         Answer questions strictly from resume context 
         """

         vector_store = FAISS.load_local(
              f"{VECTOR_DB_DIR}/{resume_id}",
              self.embeddings,
              allow_dangerous_deserialization = True
              
         )

         docs = vector_store.similarity_search(question, k = k)

         if not docs:
            return "Resume not uploaded or no information found in resume "

         context = "\n\n".join(doc.page_content for doc in docs)

         prompt = f""" 
         You are an AI assistant answering questions strictly from the given resume content.

     Rules:
     - Use ONLY the resume content below.
     - If the answer is not present, say: "Not mentioned in the resume."
     - Do NOT add extra information.
     - give answer in structured way 
     
     Resume Content:
     {context}
     
     Question:
     {question}
     
     Answer:
     """

         response = self.llm.invoke(prompt)

         return response.strip()
                      
