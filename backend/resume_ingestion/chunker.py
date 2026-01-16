from langchain.text_splitter import RecursiveCharacterTextSplitter


def chunk_resume(text:str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 150
    )

    return splitter.split_text(text)


