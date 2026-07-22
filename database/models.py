from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    DateTime
)


class Base(DeclarativeBase):
    pass


class NewsPost(Base):

    __tablename__ = "news_posts"

    id = Column(
        Integer,
        primary_key=True
    )

    title = Column(String)
    text = Column(Text)
    topic = Column(String)
    source = Column(String)
    url = Column(Text)

    sentiment = Column(String)
    confidence = Column(Float)
    processed_at = Column(DateTime)