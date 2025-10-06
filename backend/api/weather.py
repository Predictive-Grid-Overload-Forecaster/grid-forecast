from fastapi import APIRouter, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

@router.get("/weather/{city}")
def get_weather(city: str):
    """
    Fetch current + forecasted weather for a given city (using OpenWeather API).
    """
    if not WEATHER_API_KEY:
        raise HTTPException(status_code=500, detail="Missing OpenWeather API key.")

    try:
    
        geo_url = f"https://api.electricitymaps.com/v3/carbon-intensity/latest?zone=IN-NO"
        geo_response = requests.get(geo_url)
        geo_response.raise_for_status()

        geo_data = geo_response.json()
        if not geo_data:
            raise HTTPException(status_code=404, detail=f"City '{city}' not found.")

        lat, lon = geo_data[0]['lat'], geo_data[0]['lon']

        weather_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={WEATHER_API_KEY}"
        weather_response = requests.get(weather_url)
        weather_response.raise_for_status()

        weather_data = weather_response.json()

        current = weather_data["list"][0]
        forecast = weather_data["list"][1:6]  

        return {
            "city": city.title(),
            "coordinates": {"lat": lat, "lon": lon},
            "current": {
                "temperature": current["main"]["temp"],
                "feels_like": current["main"]["feels_like"],
                "humidity": current["main"]["humidity"],
                "condition": current["weather"][0]["description"],
                "wind_speed": current["wind"]["speed"]
            },
            "forecast": [
                {
                    "time": f["dt_txt"],
                    "temperature": f["main"]["temp"],
                    "condition": f["weather"][0]["description"]
                }
                for f in forecast
            ]
        }

    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=503, detail=f"Weather API request failed: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
