from langchain_community.vectorstores import FAISS
from backend.core.embeddings import get_embedding_model

def query_resume(resume_id :str,query:str,k:int = 4):
    embeddings = get_embedding_model()

    vector_store = FAISS.load_local(
        f"backend/vector_db/{resume_id}",
        embeddings,
        allow_dangerous_deserialization=True
    )

    results =  vector_store.similarity_search(query,k = k)

    return [doc.page_content for doc in results]

