import uuid

from sqlalchemy import cast, Column, Date, Index, LargeBinary, Text
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import func

from .database import Base

def create_tsvector(*args):
    exp = args[0]
    for e in args[1:]:
        exp += ' ' + e
    return func.to_tsvector('english', exp)


class Document(Base):
    __tablename__ = "document"

    id = Column(LargeBinary, primary_key=True, default=lambda: uuid.uuid4().bytes)
    day = Column(Date, nullable=False)
    author = Column(Text, nullable=False)
    body = Column(Text, nullable=False)

    __ts_vector__ = create_tsvector(
        cast(func.coalesce(body, ''), postgresql.TEXT)
    )

    __table_args__ = (
        Index(
            'idx_body_fts',
            __ts_vector__,
            postgresql_using='gin'
        ),
    )
