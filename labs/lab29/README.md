# Lab 29: API Rate Limiting in FastAPI

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab29
cd ~/python/labs/lab29
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
slowapi
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
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi.responses import JSONResponse

# Create FastAPI app
app = FastAPI(title="Rate Limiting Demo")

# Setup limiter (per client IP)
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

# Register exception handler for rate limit
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ----------- Routes -----------

@app.get("/")
def root():
    return {"message": "Welcome to Rate Limiting API"}

# Apply per-IP rate limit (5 requests per minute)
@app.get("/limited")
@limiter.limit("5/minute")
def limited_endpoint(request: Request):
    return {"message": "This is a rate-limited endpoint"}

# Different rate limit per endpoint
@app.get("/strict")
@limiter.limit("2/minute")
def strict_endpoint(request: Request):
    return {"message": "Only 2 requests per minute allowed here"}
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Step 5: Test Rate Limiting

**Normal request (works fine until limit is reached)**

```bash
curl http://127.0.0.1:8000/limited
```

**Exceed the limit (after 5 requests in a minute)**

```bash
curl http://127.0.0.1:8000/limited
```

Response:

```json
{"detail":"Rate limit exceeded: 5 per 1 minute"}
```

**Strict endpoint (only 2 per minute allowed)**

```bash
curl http://127.0.0.1:8000/strict
```

After 2 calls, response:

```json
{"detail":"Rate limit exceeded: 2 per 1 minute"}
```

---

## Step 6: Key Learning Points

* `slowapi` makes it easy to add **rate limiting in FastAPI**.
* Use **per-IP throttling** with `get_remote_address`.
* Different endpoints can have **different rate limits**.
* Can also extend for **per-user limits** by using JWT or API keys as `key_func`.

