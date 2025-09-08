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
