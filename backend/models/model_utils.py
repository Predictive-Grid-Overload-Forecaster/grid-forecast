import pandas as pd
import joblib
from pathlib import Path
from datetime import datetime

# Load LightGBM model
MODEL_PATH = Path(__file__).parent / "lgb_model.pkl"
model = joblib.load(MODEL_PATH)

# Load historical electricity data
DATA_PATH = Path(__file__).parent.parent / "data" / "electricity.csv"

def load_historical_data():
    """Load historical data lazily to avoid memory issues at startup."""
    try:
        # Load only the most recent data to reduce memory usage
        df = pd.read_csv(DATA_PATH, parse_dates=["datetime"], nrows=10000)
        df = df.sort_values("datetime").reset_index(drop=True)
        
        # Map column names to match expected feature names
        df = df.rename(columns={
            "Power demand": "demand_mw",
            "temp": "temp_c", 
            "dwpt": "dewpoint_c",
            "rhum": "rel_humidity_pct",
            "wdir": "wind_dir_deg",
            "wspd": "wind_speed_ms",
            "pres": "pressure_hpa"
        })
        return df
    except Exception as e:
        print(f"Warning: Could not load historical data: {e}")
        # Return empty dataframe with required columns
        return pd.DataFrame(columns=[
            "datetime", "demand_mw", "temp_c", "dewpoint_c", 
            "rel_humidity_pct", "wind_dir_deg", "wind_speed_ms", "pressure_hpa"
        ])

# Global variable to cache the loaded data
_df_cache = None

def get_historical_data():
    """Get historical data with caching."""
    global _df_cache
    if _df_cache is None:
        _df_cache = load_historical_data()
    return _df_cache

# Feature sets
numeric_features = [
    "demand_mw", "temp_c", "dewpoint_c", "rel_humidity_pct",
    "wind_dir_deg", "wind_speed_ms", "pressure_hpa",
    "demand_mw_lag_1", "demand_mw_lag_2", "demand_mw_lag_3",
    "demand_mw_roll_mean_3", "demand_mw_roll_mean_6", "demand_mw_roll_mean_12",
    "demand_mw_roll_std_3", "demand_mw_roll_std_6", "demand_mw_roll_std_12"
]
categorical_features = ["quarter", "hour_of_day", "day_of_week", "month"]
binary_features = ["is_weekend", "is_holiday", "is_long_weekend"]

def compute_lags_and_roll(timestamp: datetime):
    """Compute lag and rolling features from historical CSV data for a given timestamp."""
    global recent_demand_buffer
    ts = pd.Timestamp(timestamp)  # convert to pandas Timestamp
    
    # Get historical data (loaded lazily)
    df = get_historical_data()
    
    # Combine historical data with recent buffer data
    past_df = df[df["datetime"] < ts].sort_values("datetime")
    
    # Add recent buffer data if available
    recent_data = []
    for buff_ts, buff_demand in recent_demand_buffer.items():
        if buff_ts < ts:
            recent_data.append({"datetime": buff_ts, "demand_mw": buff_demand})
    
    if recent_data:
        recent_df = pd.DataFrame(recent_data)
        past_df = pd.concat([past_df, recent_df]).sort_values("datetime").reset_index(drop=True)

    if past_df.empty:
        return {f"demand_mw_lag_{i}": 0 for i in [1,2,3]} | \
               {f"demand_mw_roll_mean_{w}": 0 for w in [3,6,12]} | \
               {f"demand_mw_roll_std_{w}": 0 for w in [3,6,12]}

    # Lag features
    lags = {}
    for lag in [1,2,3]:
        lags[f"demand_mw_lag_{lag}"] = past_df["demand_mw"].iloc[-lag] if len(past_df) >= lag else past_df["demand_mw"].iloc[-1]

    # Rolling mean and std
    roll_means, roll_stds = {}, {}
    for w in [3,6,12]:
        window_vals = past_df["demand_mw"].tail(w)
        roll_means[f"demand_mw_roll_mean_{w}"] = window_vals.mean()
        roll_stds[f"demand_mw_roll_std_{w}"] = window_vals.std() if len(window_vals) > 1 else 0

    return {**lags, **roll_means, **roll_stds}

# Global buffer to store recent demand values for real-time updates
recent_demand_buffer = {}

def update_recent_demand(timestamp: datetime, actual_demand: float):
    """Update the recent demand buffer with actual demand values for real-time prediction."""
    global recent_demand_buffer
    ts = pd.Timestamp(timestamp)
    recent_demand_buffer[ts] = actual_demand
    
    # Keep only last 24 hours of data to prevent memory bloat
    cutoff_time = ts - pd.Timedelta(hours=24)
    recent_demand_buffer = {k: v for k, v in recent_demand_buffer.items() if k > cutoff_time}
