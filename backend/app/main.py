from fastapi import FastAPI

from app.database import engine
from app import models
from app.routes import auth_routes
from app.routes import auth_routes, profile_routes, habit_routes

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="CharismaFit API")

app.include_router(auth_routes.router)
app.include_router(profile_routes.router)
app.include_router(habit_routes.router)

@app.get("/")
def home():
    return {"message": "Welcome to CharismaFit"}


@app.get("/health")
def health_check():
    return {"status": "ok", "app": "CharismaFit"}