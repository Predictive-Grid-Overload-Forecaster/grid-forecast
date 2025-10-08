# Grid Forecast API Configuration Guide

## 🔧 Environment Variables Setup

To fix the API errors you're experiencing, you need to set up environment variables for the external APIs.

### 1. Create a `.env` file in the `backend` directory:

```bash
# Grid Forecast API Environment Variables
# Set your API keys here

# Calendarific API (for holidays) - Get free key at: https://calendarific.com/
CALENDARIFIC_API_KEY=your_calendarific_api_key_here
COUNTRY=IN

# OpenWeather API (for weather data) - Get free key at: https://openweathermap.org/api
WEATHER_API_KEY=your_openweather_api_key_here

# Optional: Logging level
LOG_LEVEL=INFO
```

### 2. Get API Keys:

#### Calendarific API (for holidays):
- Visit: https://calendarific.com/
- Sign up for a free account
- Get your API key
- Replace `your_calendarific_api_key_here` with your actual key

#### OpenWeather API (for weather data):
- Visit: https://openweathermap.org/api
- Sign up for a free account
- Get your API key
- Replace `your_openweather_api_key_here` with your actual key

### 3. Restart the Server:

After setting up the environment variables, restart your server:

```bash
# Stop the current server (Ctrl+C)
# Then restart:
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
```

## 🚨 Issues Fixed:

### 1. Memory Error in Prediction Endpoint ✅
- **Problem**: `"Error tokenizing data. C error: out of memory"`
- **Solution**: Limited CSV loading to 10,000 rows and added error handling
- **Status**: Fixed - prediction endpoint now works without memory issues

### 2. Missing Environment Variables ✅
- **Problem**: `"Country not set in environment variables"`
- **Solution**: Added better error messages and configuration guide
- **Status**: Fixed - clear instructions provided

### 3. Weather API Authentication ✅
- **Problem**: `"401 Client Error: Unauthorized"`
- **Solution**: Added proper error handling for missing API keys
- **Status**: Fixed - clear error messages provided

## 🧪 Testing Your Setup:

1. **Test Prediction Endpoint** (should work without API keys):
   ```bash
   curl -X POST "http://localhost:8000/api/predict" \
        -H "Content-Type: application/json" \
        -d '{
          "timestamp": "2024-01-01T14:00:00",
          "weather": {
            "temp_c": 25.0,
            "dewpoint_c": 20.0,
            "rel_humidity_pct": 60.0,
            "wind_dir_deg": 180.0,
            "wind_speed_ms": 5.0,
            "pressure_hpa": 1013.0
          },
          "binary": {
            "is_weekend": 0,
            "is_holiday": 0,
            "is_long_weekend": 0
          },
          "categorical": {
            "quarter": 1,
            "hour_of_day": 14,
            "day_of_week": 1,
            "month": 1
          },
          "current_demand": 2000.0
        }'
   ```

2. **Test Holidays Endpoint** (after setting API keys):
   ```bash
   curl "http://localhost:8000/api/holidays/2024"
   ```

3. **Test Weather Endpoint** (after setting API keys):
   ```bash
   curl "http://localhost:8000/api/weather/Delhi"
   ```

## 📊 Current Status:

- ✅ **Prediction Endpoint**: Working (no API keys required)
- ⚠️ **Holidays Endpoint**: Needs Calendarific API key
- ⚠️ **Weather Endpoint**: Needs OpenWeather API key
- ✅ **Carbon Endpoint**: Working (uses local data)

## 🎯 Next Steps:

1. Create the `.env` file with your API keys
2. Restart the server
3. Test all endpoints
4. Your Grid Forecast API will be fully functional!
