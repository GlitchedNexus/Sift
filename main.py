from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"SIFT": "Welcome to Sift! Please authenticate"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.post("/items/new/{item_id}")
def add_itep():
    return {"status": "ok"}
