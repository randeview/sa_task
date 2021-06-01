from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Bye": "World"}


@app.get("/health/")
def read_item():
    return {"status": "ok"}
