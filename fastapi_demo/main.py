from fastapi import FastAPI, Depends
from fastapi_demo import models
from fastapi_demo.movie import Movie
from fastapi_demo.database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/movies")
def get_movies(db: Session = Depends(get_db)):
    return db.query(models.Movie).all()

@app.post("/movies")
def create_movie(movie: Movie, db: Session = Depends(get_db)):
    movie_model = models.Movie()
    movie_model.title = movie.title
    movie_model.year = movie.year
    movie_model.rating = movie.rating

    db.add(movie_model)
    db.commit()

    return movie