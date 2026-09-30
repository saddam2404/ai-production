from fastapi import FastAPI,Depends,UploadFile,File,HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Document
from app.schemas import DocumentResponse
import shutil
import os
from app.aws import s3_client, BUCKET_NAME

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

@app.get("/documents", response_model=list[DocumentResponse])
def get_documents(db: Session = Depends(get_db)):
    Documents = db.query(Document).all()
    return Documents

@app.post("/documents",)
def upload_document(file: UploadFile =File(...),
                    db: Session = Depends(get_db)):
    s3_client.upload_fileobj(file.file, 
                             BUCKET_NAME, 
                             file.filename)
    new_document = Document(
    filename=file.filename,
    file_path=file.filename
)

    db.add(new_document)
    db.commit()
    db.refresh(new_document)


    return{
        "filename": new_document.filename,
        "id": new_document.id,
        "content_type": file.content_type,
        "saved to": file.filename
    }
@app.get("/documents/{document_id}")
def get_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@app.delete("/documents/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    document = db.query(Document).filter(Document.id == document_id).first()
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    if os.path.exists(document.file_path):
        os.remove(document.file_path)
    db.delete(document)
    db.commit()
    return {"message": "Document deleted successfully"}