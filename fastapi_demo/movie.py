from pydantic import BaseModel, Field

class Movie(BaseModel):
    title: str = Field(min_length=1)
    year: int = Field(gt=-1, lt=10001)
    rating: float = Field(gt=-1, lt=11)