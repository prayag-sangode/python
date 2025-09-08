# Lab 27: API Documentation with FastAPI

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab27
cd ~/python/labs/lab27
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
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Step 5: Access API Documentation

FastAPI automatically provides **interactive documentation**:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
* OpenAPI JSON spec: [http://127.0.0.1:8000/openapi.json](http://127.0.0.1:8000/openapi.json)

---

## Step 6: Test API

### Create Item

```bash
curl -X POST "http://127.0.0.1:8000/items/" \
-H "Content-Type: application/json" \
-d '{"name":"Laptop","price":1200}'
```

**Expected Output:**

```json
{
  "name": "Laptop",
  "price": 1200.0
}
```

---

### Key Learning Points

* FastAPI **automatically generates Swagger/OpenAPI docs**
* `/docs` → Swagger UI
* `/redoc` → ReDoc documentation
* You can **customize metadata** (`title`, `description`, `version`, `contact`, `license`)
* Tags, summaries, and docstrings appear in docs automatically

