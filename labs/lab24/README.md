# Lab 24: FastAPI Request Body & Response Models

This lab introduces **Pydantic models** for **request body validation** and **response models** in FastAPI.

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab24
cd ~/python/labs/lab24
```

---

## Step 2: Setup Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

Create **requirements.txt**:

```bash
cat >> requirements.txt << EOF
fastapi
uvicorn
EOF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Step 3: Create FastAPI App `main.py`

```bash
cat >> main.py << EOF
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
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

* Server runs at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
* Interactive docs available:

  * Swagger UI: `http://127.0.0.1:8000/docs`
  * Redoc: `http://127.0.0.1:8000/redoc`

> Press `Ctrl+C` to stop the server when done.

---

## Step 5: Test Endpoint

### 1️⃣ POST `/items/` with valid JSON body

```bash
curl -X POST "http://127.0.0.1:8000/items/" \
-H "Content-Type: application/json" \
-d '{"name":"Laptop","description":"Gaming laptop","price":1000,"tax":100}'
```

**Expected Output:**

```json
{
  "name": "Laptop",
  "price_with_tax": 1100
}
```

### 2️⃣ Validation Example: Missing or Invalid Fields

```bash
curl -X POST "http://127.0.0.1:8000/items/" \
-H "Content-Type: application/json" \
-d '{"description":"No name","price":"abc"}'
```

**Expected Output:**

```json
{
  "detail": [
    {
      "loc": ["body", "name"],
      "msg": "field required",
      "type": "value_error.missing",
      "input": {"description":"No name","price":"abc"}
    },
    {
      "loc": ["body", "price"],
      "msg": "value is not a valid float",
      "type": "type_error.float",
      "input": "abc"
    }
  ]
}
```

---

### ✅ Key Learning Points

* **Pydantic models** validate input automatically
* **Optional fields** can have defaults
* **Response models** enforce output schema (`response_model=ItemResponse`)
* FastAPI automatically handles **data validation errors** and returns structured messages

---

## Step 6: Cleanup (Optional)

```bash
deactivate
```
