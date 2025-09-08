# Lab 30: Logging & Monitoring in FastAPI

---

## Step 1: Create Project Directory

```bash
mkdir -p ~/python/labs/lab30
cd ~/python/labs/lab30
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
python-json-logger
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
import logging
import time
from fastapi import FastAPI, Request, Response
from pythonjsonlogger import jsonlogger

# Configure JSON logger
logger = logging.getLogger("api_logger")
logger.setLevel(logging.INFO)

logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter("%(asctime)s %(levelname)s %(message)s")
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

app = FastAPI(title="Logging & Monitoring Demo")

# Middleware to log requests & responses
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    # Process request
    response: Response = await call_next(request)
    process_time = time.time() - start_time
    
    # Log request & response info in JSON
    logger.info({
        "method": request.method,
        "url": str(request.url),
        "status_code": response.status_code,
        "process_time": round(process_time, 4),
        "client_host": request.client.host
    })
    
    return response

# Routes
@app.get("/", tags=["General"])
def root():
    return {"message": "Logging demo running"}

@app.get("/items/{item_id}", tags=["Items"])
def get_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
EOF
```

---

## Step 4: Run the FastAPI App

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## Step 5: Test API & Observe Logs

### Request

```bash
curl "http://127.0.0.1:8000/items/1?q=test"
```

### Expected Response

```json
{"item_id":1,"query":"test"}
```

### Logs (JSON format in terminal)

```json
{"asctime": "2025-09-08 12:10:00,123", "levelname": "INFO", "message": {"method": "GET", "url": "http://127.0.0.1:8000/items/1?q=test", "status_code": 200, "process_time": 0.0021, "client_host": "127.0.0.1"}}
```

---

## Step 6: Key Learning Points

* Used **python-json-logger** to log structured data in JSON.
* Logged request **method, URL, status\_code, response time, client IP**.
* JSON logs are easy to ship to **Elasticsearch, Loki, Splunk, or Cloud Logging**.
* Middleware makes it possible to **trace every request globally**.
