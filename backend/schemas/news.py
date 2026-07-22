from pydantic import BaseModel


class NewsResponse(BaseModel):
    id: int
    title: str
    topic: str
    sentiment: str | None
    confidence: float | None

    class Config:
        from_attributes = True