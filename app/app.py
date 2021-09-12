from datetime import datetime

from fastapi import FastAPI
from fastapi.params import Depends
from pydantic import BaseModel
from sqlalchemy.orm.session import Session

from . import database, models

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.on_event("startup")
def startup_event():
    doc1 = models.Document(
        day=datetime(2021, 9, 11),
        author="Stig Engstöm",
        body="Jag lever.",
    )
    db = database.SessionLocal()
    db.add(doc1)
    db.commit()
    db.close()


@app.get("/")
async def root():
    return {"message": "Hello World"}

class Document(BaseModel):
    author: str
    date: str
    body: str

@app.post("/documents")
async def create_document(document: Document, db: Session = Depends(database.get_db)):
    doc = models.Document(
        author=document.author,
        day=document.date,
        body=document.body,
    )
    db.add(doc)
    db.commit()


@app.get("/documents")
async def get_documents(search_string: str, db: Session = Depends(database.get_db)):
    documents = db.query(models.Document).filter(models.Document.__ts_vector__.match(search_string, postgresql_regconfig='english')).all()
    documents = [
        Document(
            author=doc.author,
            date=str(doc.day),
            body=doc.body,
        )
        for doc in documents
    ]
    return documents
