from fastapi import FastAPI
from fastapi.responses import FileResponse
from loader import load_data
from search import search_dataset

app = FastAPI()

# Load CSVs once at startup
load_data()


@app.get("/")
def home():
    return FileResponse("front.html")


@app.get("/search")
def search(table: str, query: str):

    results = search_dataset(table, query)

    if not results:
        return []

    return results