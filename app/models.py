import uuid

from sqlalchemy import Column, Date, LargeBinary, Text

from .database import Base

class Document(Base):
    __tablename__ = "document"

    id = Column(LargeBinary, primary_key=True, default=lambda: uuid.uuid4().bytes)
    day = Column(Date, nullable=False)
    author = Column(Text, nullable=False)
    body = Column(Text, nullable=False)
