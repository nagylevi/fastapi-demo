from sqlalchemy import Column, Integer, String, Float
from fastapi_demo.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    year = Column(Integer)
    rating = Column(Float)