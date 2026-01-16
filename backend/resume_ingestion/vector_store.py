from langchain_community.vectorstores import FAISS
from langchain.schema import Document
from backend.core.embeddings import get_embedding_model
import os

VECTOR_DB_DIR ="backend/vector_db"

def build_vector_store(chunks: list[str], resume_id: str) -> str:
    """
    Builds a FAISS vector store from resume chunks.
    """
    os.makedirs(VECTOR_DB_DIR,exist_ok=True)
    # 1️⃣ Convert chunks → Documents
    documents = [
        Document(
            page_content=chunk,
            metadata={
                "resume_id": resume_id,
                "chunk_id": i
            }
        )
        for i, chunk in enumerate(chunks)
    ]

    # 2️⃣ Get embedding model
    embeddings = get_embedding_model()

    # 3️⃣ Create FAISS vector store
    vector_store = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    save_path = os.path.join(VECTOR_DB_DIR,resume_id)
    vector_store.save_local(save_path)

    return save_path
