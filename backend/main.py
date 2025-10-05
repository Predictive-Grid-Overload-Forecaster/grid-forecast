from fastapi import FastAPI
from .api.holidays import router as holidays_router

app = FastAPI(
    title="Grid Forecast API",
    description="API for electricity demand prediction and related data.",
    version="0.1.0",
)

@app.get("/ping")
def ping():
    return {"status": "ok", "message": "Ping!"}

@app.get("/")
def root():
    return {"message": "API is running"}

app.include_router(holidays_router, prefix="/api")
