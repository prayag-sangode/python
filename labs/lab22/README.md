# Lab 22: FastAPI Hello World

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab22
cd ~/python/labs/lab22
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

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI World!"}
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

* Server runs at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**
* FastAPI **interactive docs** are available at:

  * Swagger UI: `http://127.0.0.1:8000/docs`
  * Redoc: `http://127.0.0.1:8000/redoc`

---

## Step 5: Test the GET Endpoint

```bash
curl http://127.0.0.1:8000/
```

**Expected Output:**

```json
{"message":"Hello, FastAPI World!"}
```

---

### Key Learning Points

* **FastAPI app** initialization
* Define a **GET endpoint** with a function
* Return **JSON response** automatically
* FastAPI provides **interactive API docs** out-of-the-box
