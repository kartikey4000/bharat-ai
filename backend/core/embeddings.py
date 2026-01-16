from langchain_community.embeddings import FakeEmbeddings

def get_embedding_model():
    """
    TEMP embedding model (no torch, no OpenAI)
    Used only to validate pipeline
    """
    return FakeEmbeddings(size=384)
