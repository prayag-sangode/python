# Lab 23: FastAPI Path & Query Parameters

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab23
cd ~/python/labs/lab23
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
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

* Server runs at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
* Interactive docs:

  * Swagger UI: `http://127.0.0.1:8000/docs`
  * Redoc: `http://127.0.0.1:8000/redoc`

---

## Step 5: Test Endpoints

### Path Parameter

```bash
curl http://127.0.0.1:8000/items/5
```

**Output:**

```json
{"item_id":5,"message":"Item ID is 5"}
```

### Query Parameter

```bash
curl "http://127.0.0.1:8000/search/?q=fastapi&limit=3"
```

**Output:**

```json
{"query":"fastapi","limit":3,"message":"Searching for 'fastapi' with limit 3"}
```

* Default values also work:

```bash
curl "http://127.0.0.1:8000/search/"
```

```json
{"query":null,"limit":10,"message":"Searching for 'None' with limit 10"}
```

---

### Key Learning Points

* Use **path parameters** for dynamic URLs (`/items/{item_id}`)
* Use **query parameters** for optional filters (`?q=fastapi&limit=3`)
* FastAPI automatically **validates types** (`int`, `str`, etc.)
* Optional parameters can have **default values** using `Optional[...]`

