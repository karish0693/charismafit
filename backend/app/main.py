from fastapi import FastAPI

app = FastAPI(title="CharismaFit API")

@app.get("/")
def home():
    return {"message": "Welcome to CharismaFit"}

@app.get("/health")
def health_check():
    return {"status": "ok", "app": "CharismaFit"}