from datetime import datetime

from fastapi import FastAPI

from . import database, models

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
