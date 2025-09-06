from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Pydantic model for request body
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Pydantic model for response
class ItemResponse(BaseModel):
    name: str
    price_with_tax: float

# POST endpoint with request body validation
@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    price_with_tax = item.price + (item.tax if item.tax else 0)
    return ItemResponse(name=item.name, price_with_tax=price_with_tax)
