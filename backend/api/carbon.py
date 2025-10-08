from fastapi import APIRouter
import pandas as pd
import os

router = APIRouter(prefix="/carbon", tags=["Carbon Data"])

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "electricity.csv")

def get_data():
    """Load data lazily to avoid memory issues at startup."""
    df = pd.read_csv(DATA_PATH)
    df['datetime'] = pd.to_datetime(df['datetime'])
    
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

EMISSION_FACTOR = 820
RENEWABLE_PCT = 42.5

@router.get("/delhi")
def get_carbon_data():
    """Return estimated carbon intensity and renewable % for Delhi based on power demand"""
    
    df = get_data()  # Load data only when needed
    latest = df.sort_values('datetime', ascending=False).head(1)
    demand_mw = latest['demand_mw'].values[0]

    carbon_intensity = round(demand_mw * EMISSION_FACTOR, 2)
    
    timestamp = str(latest['datetime'].values[0])
    
    return {
        "region": "Delhi",
        "timestamp": timestamp,
        "carbon_intensity_gco2_per_kwh": carbon_intensity,
        "pct_renewable": RENEWABLE_PCT
    }



# Average grid emission factor in India = (gCO2/kWh)
# Convert MW to kWh for 5-minute interval: MW * 1/12 h = MWh
# But since gCO2/kWh is per kWh, multiply demand in MW by 1000 to get kW
# Simplified: just scale with demand
#Estimate carbon intensity using a fixed emission factor per MW demand (India average grid factor ≈ 0.82 kg CO₂/kWh or 820 gCO₂/kWh).
#Formula: carbon intensity (gCO₂/kWh)=Power demand (MW)×820
