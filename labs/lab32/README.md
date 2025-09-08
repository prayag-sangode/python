# Lab 32: API Key Authentication with FastAPI

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab32
cd ~/python/labs/lab32
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
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

app = FastAPI(title="API Key Authentication Demo")

# Define API Key header
API_KEY = "mysecretkey123"
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# Dependency function to validate API key
def get_api_key(api_key: str = Security(api_key_header)):
    if api_key == API_KEY:
        return api_key
    raise HTTPException(
        status_code=HTTP_403_FORBIDDEN,
        detail="Could not validate API KEY"
    )

@app.get("/")
def root():
    return {"message": "Public endpoint - no authentication required"}

@app.get("/secure-data")
def secure_data(api_key: str = Depends(get_api_key)):
    return {"message": "This is protected data", "api_key_used": api_key}
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Step 5: Test API Key Authentication

### 1. Public endpoint (no key required)

```bash
curl http://127.0.0.1:8000/
```

**Expected Output:**

```json
{"message":"Public endpoint - no authentication required"}
```

---

### 2. Secure endpoint with **correct key**

```bash
curl -H "X-API-Key: mysecretkey123" http://127.0.0.1:8000/secure-data
```

**Expected Output:**

```json
{
  "message": "This is protected data",
  "api_key_used": "mysecretkey123"
}
```

---

### 3. Secure endpoint with **wrong key**

```bash
curl -H "X-API-Key: wrongkey" http://127.0.0.1:8000/secure-data
```

**Expected Output:**

```json
{
  "detail": "Could not validate API KEY"
}
```

---

### 4. Secure endpoint with **no key**

```bash
curl http://127.0.0.1:8000/secure-data
```

**Expected Output:**

```json
{
  "detail": "Could not validate API KEY"
}
```

---

## Step 6: Key Learning Points

* FastAPI provides `APIKeyHeader` for **header-based API key validation**.
* Endpoints can be **public** or **protected** using dependencies.
* Missing or invalid keys return **403 Forbidden**.
* API Keys should normally be stored securely (e.g., **environment variables or secret manager**).

