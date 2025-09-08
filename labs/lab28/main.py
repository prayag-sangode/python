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
