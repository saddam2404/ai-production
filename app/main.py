from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Document

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/doc1")
def get_documentation():
    return {"item": "This is the documentation for the API."}

# @app.get("/documents")
# def get_documents(db: Session = Depends(get_db)):
#     return []

@app.get("/documents")
def get_documents(db: Session = Depends(get_db)):
    Documents = db.query(Document).all()
    return Documents