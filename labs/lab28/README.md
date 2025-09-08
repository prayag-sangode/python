# Lab 28: Error Handling & Middleware in FastAPI

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab28
cd ~/python/labs/lab28
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
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import time

app = FastAPI(title="Error Handling & Middleware Demo")

# ---------- Global Exception Handling ----------
@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"error": "Invalid value provided", "details": str(exc)},
    )

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "details": str(exc)},
    )

# ---------- Custom Middleware ----------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"➡️ {request.method} {request.url} - Completed in {process_time:.4f}s")
    response.headers["X-Process-Time"] = str(process_time)
    return response

# ---------- Routes ----------
@app.get("/divide")
def divide_numbers(a: int, b: int):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return {"result": a / b}

@app.get("/error")
def trigger_error():
    raise RuntimeError("Unexpected error occurred!")
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Step 5: Test Endpoints

✅ **Success case**

```bash
curl "http://127.0.0.1:8000/divide?a=10&b=2"
```

Response:

```json
{"result": 5.0}
```

❌ **Handled ValueError**

```bash
curl "http://127.0.0.1:8000/divide?a=10&b=0"
```

Response:

```json
{"error":"Invalid value provided","details":"Division by zero is not allowed"}
```

❌ **Global Exception**

```bash
curl "http://127.0.0.1:8000/error"
```

Response:

```json
{"error":"Internal Server Error","details":"Unexpected error occurred!"}
```

---

## Step 6: Verify Middleware

Check terminal logs:

```
➡️ GET http://127.0.0.1:8000/divide?a=10&b=2 - Completed in 0.0012s
```

Response headers include:

```
X-Process-Time: 0.0012
```

---

## Key Learning Points

* Use **exception handlers** for global error handling.
* Use **middleware** to log, monitor, or modify requests/responses.
* Response headers can include **custom metadata** (e.g., execution time).
