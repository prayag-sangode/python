from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# --- Path Parameter ---
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "message": f"Item ID is {item_id}"}

# --- Query Parameter ---
@app.get("/search/")
def search_item(q: Optional[str] = None, limit: int = 10):
    return {"query": q, "limit": limit, "message": f"Searching for '{q}' with limit {limit}"}
