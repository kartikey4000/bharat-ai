from backend.resume_ingestion.chunker import chunk_resume
from backend.resume_ingestion.cleaner import clean_text
from backend.resume_ingestion.loader import load_resume
from backend.core.embeddings import get_embedding_model
from backend.resume_ingestion.vector_store import build_vector_store
from datetime import datetime
from pathlib import Path
import json
import uuid
import shutil


def ingest_resume(file_path: str) -> dict:
    raw_text = load_resume(file_path)
    if not raw_text.strip():
        raise ValueError("Resume text is empty")

    cleaned_text = clean_text(raw_text)
    chunks = chunk_resume(cleaned_text)

    resume_id = str(uuid.uuid4())
    embedding = get_embedding_model()

   
    vector_path = build_vector_store(
        chunks=chunks,
        resume_id=resume_id
    )

   
    resume_dir = Path(vector_path)
    resume_dir.mkdir(parents=True, exist_ok=True)

    pdf_path = resume_dir / "resume.pdf"
    shutil.move(file_path, pdf_path)

    
    meta_path = resume_dir / "meta.json"
    meta_path.write_text(json.dumps({
        "uploaded_at": datetime.utcnow().isoformat()
    }))

    return {
        "status": "ingested",
        "resume_id": resume_id,
        "num_chunks": len(chunks),
        "vector_path": str(resume_dir)
    }



