from fastapi import FastAPI

app = FastAPI(title="FastAPI with Nginx Gateway")

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

@app.get("/service")
def service():
    return {"message": "This is the service endpoint"}
