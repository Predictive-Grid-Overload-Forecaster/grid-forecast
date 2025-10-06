from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import logging
from .predict import predict
from .model_utils import update_recent_demand

# Setup FastAPI
app = FastAPI(title="Delhi Grid Forecaster - LightGBM")

# Configure logging
logging.basicConfig(level=logging.INFO)

# --- Pydantic models ---
class Weather(BaseModel):
    temp_c: float
    dewpoint_c: Optional[float] = None
    rel_humidity_pct: Optional[float] = None
    wind_dir_deg: Optional[float] = None
    wind_speed_ms: Optional[float] = None
    pressure_hpa: Optional[float] = None

class BinaryFlags(BaseModel):
    is_weekend: int
    is_holiday: int
    is_long_weekend: int

class CategoricalFeatures(BaseModel):
    quarter: int
    hour_of_day: int
    day_of_week: int
    month: int

class PredictRequest(BaseModel):
    timestamp: datetime
    weather: Weather
    binary: BinaryFlags
    categorical: CategoricalFeatures
    current_demand: Optional[float] = 0
    actual_demand: Optional[float] = None

# --- Prediction endpoint ---
@app.post("/predict")
def make_prediction(req: PredictRequest):
    try:
        logging.info(f"Received prediction request for timestamp: {req.timestamp}")
        logging.info(f"Weather data: {req.weather.dict()}")
        logging.info(f"Binary flags: {req.binary.dict()}")
        logging.info(f"Categorical features: {req.categorical.dict()}")
        logging.info(f"Current demand: {req.current_demand}")

        # Run prediction
        pred = predict(
            req.timestamp,
            req.weather.dict(),
            req.binary.dict(),
            req.categorical.dict(),
            req.current_demand
        )

        logging.info(f"Prediction result: {pred}")

        # Update recent demand buffer if provided
        if req.actual_demand is not None:
            update_recent_demand(req.timestamp, req.actual_demand)
            logging.info(f"Updated recent demand with actual_demand={req.actual_demand}")

        return {
            "timestamp": req.timestamp.isoformat(),
            "predicted_demand_mw": pred
        }

    except Exception as e:
        logging.exception("Prediction failed due to an error")
        return {"error": str(e)}
