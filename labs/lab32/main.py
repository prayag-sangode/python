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
