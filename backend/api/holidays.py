from fastapi import APIRouter, HTTPException
import requests
import os
from dotenv import load_dotenv

load_dotenv()  

router = APIRouter()

CALENDARIFIC_API_KEY = os.getenv("CALENDARIFIC_API_KEY")
COUNTRY = os.getenv("COUNTRY")


@router.get("/holidays/{year}")
def get_holidays(year: int):

    if not CALENDARIFIC_API_KEY:
        raise HTTPException(status_code=500, detail="API key not set in environment variables.")
    
    if year < 1900 or year > 2100:
        raise HTTPException(status_code=400, detail="Invalid year. Please provide a year between 1900 and 2100.")
    
    if not COUNTRY:
        raise HTTPException(status_code=500, detail="Country not set in environment variables.")
    
    url = f"https://calendarific.com/api/v2/holidays?api_key={CALENDARIFIC_API_KEY}&country={COUNTRY}&year={year}"
    
    try:
        response = requests.get(url, timeout=10) 
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Failed to fetch holidays: {str(e)}")
    
    data = response.json()
    
    if data.get("meta", {}).get("code") != 200:
        message = data.get("meta", {}).get("error_detail", "Unknown API error")
        raise HTTPException(status_code=502, detail=f"Calendarific API error: {message}")
    
    return data
