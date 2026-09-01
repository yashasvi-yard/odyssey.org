# ingestion
# auth
# extraction
# search?
# Develop a comprehensive outreach portal that archives expedition reports, scientific datasets, publications, photographs, videos and institutional activities while generating content for websites and social media.

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

@app.get("/")
async def ping():
    return {
        "status": "Odyssey begins"
    }

@app.post("/upload")
async def upload(file:UploadFile=File(...)):
    return {
        "file name":file.filename,
        "file size":f"{file.size/(1024 * 1024)} MB",
        "file type":file.content_type
    }
