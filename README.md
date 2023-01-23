# FastAPI REST API demo app

## Run project

```cmd
uvicorn fastapi_demo.main:app --reload
```

You can access the app in the browser: <http://localhost:8000>.

## Load database

You can load database (data is scraped from imdb top 250 movies <http://www.imdb.com/chart/top>)
by running the script `load_database.py`