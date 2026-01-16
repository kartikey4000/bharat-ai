from fastapi import APIRouter,UploadFile,HTTPException,File
import shutil
import os
import uuid
from pydantic import BaseModel
from backend.resume_ingestion.query import query_resume

from backend.resume_ingestion.service import ingest_resume

#---------------------------------------------------------


router = APIRouter()

UPLOAD_DIR = "temp_resumes"
os.makedirs(UPLOAD_DIR,exist_ok=True)

@router.post("/resume/upload")
async def upload_resume(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400,detail="Only pdf are allowed to be uplaoded")

    
    file_id = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join(UPLOAD_DIR,file_id)


    try:
       with open(file_path,"wb") as buffer:
           shutil.copyfileobj(file.file,buffer)
   
       result = ingest_resume(file_path)

       return {
         "status": "success",
         "resume_id": result["resume_id"],
         "filename": file.filename,
         "num_chunks": result["num_chunks"]
       }

    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))

    finally:

        if os.path.exists(file_path):
            os.remove(file_path)


#------------------------------------------------------------------

class ResumeQuery(BaseModel):
    resume_id : str
    question: str
    k:int = 4


@router.post("/resume/query")
def query_uploaded_resume(payload: ResumeQuery):
    try:
        answers = query_resume(
            resume_id = payload.resume_id,
            query = payload.question,
            k = payload.k
        )

        return {
              
              "resume_id":payload.resume_id,
              "answers":answers
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




