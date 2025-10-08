from datetime import datetime
import pandas as pd
from .model_utils import model, numeric_features, categorical_features, binary_features, compute_lags_and_roll

def make_features(timestamp: datetime, weather: dict, binary: dict, categorical: dict, current_demand: float = 0):
    """Prepare a single-row DataFrame for LightGBM prediction."""
    features = compute_lags_and_roll(timestamp)
    features["demand_mw"] = current_demand

    # Merge all feature groups
    features.update({
        "temp_c": weather.get("temp_c", 0),
        "dewpoint_c": weather.get("dewpoint_c", 0),
        "rel_humidity_pct": weather.get("rel_humidity_pct", 0),
        "wind_dir_deg": weather.get("wind_dir_deg", 0),
        "wind_speed_ms": weather.get("wind_speed_ms", 0),
        "pressure_hpa": weather.get("pressure_hpa", 0),
        **binary,
        **categorical
    })

    # Ensure column order and missing columns filled
    final_features = numeric_features + categorical_features + binary_features
    df_row = pd.DataFrame([features])
    df_row = df_row.reindex(columns=final_features, fill_value=0)
    return df_row

def predict(timestamp: datetime, weather: dict, binary: dict, categorical: dict, current_demand: float = 0):
    """Run inference with LightGBM model."""
    df_row = make_features(timestamp, weather, binary, categorical, current_demand)
    prediction = model.predict(df_row)[0]
    return float(prediction)
