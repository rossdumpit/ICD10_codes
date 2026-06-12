from fastapi import FastAPI
from fastapi.responses import FileResponse
from loader import load_data
from search import search_dataset
import os
import sys

app = FastAPI()

load_data()


def resource_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.dirname(__file__), filename)


@app.get("/")
def home():
    return FileResponse(resource_path("front.html"))


@app.get("/search")
def search(table: str, query: str):

    results = search_dataset(table, query)

    if not results:
        return []

    return results
