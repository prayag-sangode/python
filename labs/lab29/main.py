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
