from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="My API Documentation Demo",
    description="This is an example API with Swagger/OpenAPI docs",
    version="1.0.0",
    contact={
        "name": "DevOps Engineer",
        "email": "devops@example.com"
    },
    license_info={
        "name": "MIT",
    },
)

# Pydantic model for input
class Item(BaseModel):
    name: str
    price: float

# Routes with docstrings & summaries
@app.get("/", tags=["General"], summary="Root Endpoint")
def read_root():
    """Root endpoint to test if the API is running."""
    return {"message": "Welcome to the API"}

@app.post("/items/", response_model=Item, tags=["Items"], summary="Create Item")
def create_item(item: Item):
    """
    Create a new item with **name** and **price**.

    - **name**: Name of the item
    - **price**: Price as a float
    """
    return item
