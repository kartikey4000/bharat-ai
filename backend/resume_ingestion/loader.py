from langchain.document_loaders import PyPDFLoader

def load_resume(file_path:str)->str:
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    
    full_text = "/n".join([page.page_content for page in pages])
    return full_text
    