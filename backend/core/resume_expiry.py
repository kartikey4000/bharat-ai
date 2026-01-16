from datetime import datetime, timedelta
from pathlib import Path
import json
import shutil
from fastapi import HTTPException

EXPIRY_HOURS = 3

def ensure_resume_not_expired(resume_id: str):
    resume_dir = Path(f"vector_db/{resume_id}")
    meta_file = resume_dir / "meta.json"

    if not resume_dir.exists() or not meta_file.exists():
        raise HTTPException(404, "Resume not found")

    meta = json.loads(meta_file.read_text())
    uploaded_at = datetime.fromisoformat(meta["uploaded_at"])

    if datetime.utcnow() > uploaded_at + timedelta(hours=EXPIRY_HOURS):
        shutil.rmtree(resume_dir)

        raise HTTPException(
            status_code=410,
            detail="Resume expired. Please upload again."
        )
