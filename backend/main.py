from fastapi import FastAPI

app = FastAPI(
    title="Grid Forecast API",
    description="API for electricity demand prediction and related data.",
    version="0.1.0",
)


@app.get("/ping")
def ping():
    """
    A simple health-check endpoint to verify the API is running.
    """
    return {"status": "ok", "message": "Ping!"}

