from fastapi import FastAPI
from .api.holidays import router as holidays_router
from .api.weather import router as weather_router
from .api.carbon import router as carbon_router  

app = FastAPI(
    title="Grid forecast API",
    description="API for electricity demand prediction and related data.",
    version="0.1.0",
)

@app.get("/ping")
def ping():
    return {"status": "ok", "message": "Ping!"}

@app.get("/")
def root():
    return {"message": "API is running"}

# Include routers
app.include_router(holidays_router, prefix="/api")
app.include_router(weather_router, prefix="/api")
app.include_router(carbon_router, prefix="/api")  # ✅ now works
