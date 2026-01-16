
from dotenv import load_dotenv
load_dotenv() 
from fastapi.middleware.cors import CORSMiddleware

from backend.core.env_fix import disable_proxies
disable_proxies()  # <


from fastapi import FastAPI
from backend.resume_ingestion.chat import router as chat_router
from backend.api.resume import router as resume_router

app = FastAPI(title = "Bharat API")

@app.get("/")
def root():
    return {"status": "Bharat AI backend running 🚀"}


#app.include_router(chat_router)

app.include_router(resume_router)
app.include_router(chat_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],

)



