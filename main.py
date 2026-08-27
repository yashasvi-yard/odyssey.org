# ingestion
# auth
# extraction
# search?
# Develop a comprehensive outreach portal that archives expedition reports, scientific datasets, publications, photographs, videos and institutional activities while generating content for websites and social media.

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "Odyssey begins",
    }
