import redis
from app.aws import s3_client, BUCKET_NAME
from pypdf import PdfReader

from app.database import SessionLocal
from app.models import Document, DocumentChunk

redis_client = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True  # Automatically decode byte responses to strings
)
while True:
    task = redis_client.brpop('document_queue', timeout=0)  # Wait indefinitely for a task
    filename = task[1]

    db = SessionLocal()
    document = db.query(Document).filter(
        Document.filename == filename).first()
    if document is None:
        print("Document not found in the database. Skipping processing for:", filename)
        db.close()
        continue
    document_id = document.id
    print("Processing document:", filename, "with ID:", document_id)

    file_path = f"downloads/{filename}"
    s3_client.download_file(BUCKET_NAME, filename, file_path)

    reader = PdfReader(file_path)  # This will raise an error if the PDF is corrupted or unreadable
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    # print("Extracted text from page:", page.extract_text())

    # chunks = text.split(",")
    # for chunk in chunks:
    #     if chunk.strip():  # Avoid adding empty chunks
    #         print("CHUNKS:", chunk.strip())

    chunk_size = 500
    overlap = 100

    step = chunk_size - overlap

    chunks = []

    for i in range(0, len(text), step):
        chunk = text[i:i + chunk_size]
        if chunk.strip():  # Avoid adding empty chunks
            chunks.append(chunk.strip())
        
    print("Total chunks created:", len(chunks))
    

    db.query(DocumentChunk).filter(DocumentChunk.document_id == document_id).delete(synchronize_session=False)

    for chunk in chunks:
        new_chunk = DocumentChunk(
            document_id=document_id, 
            chunk_text=chunk)
        db.add(new_chunk)

    db.commit()
    print("Saved chunk to database:", len(chunks))
    db.close()

    for chunk in chunks:
        print("CHUNKS:", chunk)

    print("Processing task:", task[1])
