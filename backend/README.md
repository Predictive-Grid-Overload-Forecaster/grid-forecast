# Grid Forecast Backend

This is the backend API for the Grid Forecast application, providing electricity demand prediction using a LightGBM model.

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Server
```bash
python start_server.py
```
Or manually:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. Test the Setup
```bash
python test_model.py
```

## 📊 API Endpoints

### Core Endpoints
- `GET /` - API status
- `GET /ping` - Health check
- `POST /api/predict` - Make electricity demand prediction

### Data Endpoints
- `GET /api/holidays/{year}` - Get holidays for a year
- `GET /api/weather/{city}` - Get weather data for a city
- `GET /api/carbon/delhi` - Get carbon intensity data for Delhi

## 🔧 Model Architecture

### Features Used
- **Numeric Features (16)**: demand_mw, temp_c, dewpoint_c, rel_humidity_pct, wind_dir_deg, wind_speed_ms, pressure_hpa, lag features (1,2,3), rolling means (3,6,12), rolling stds (3,6,12)
- **Categorical Features (4)**: quarter, hour_of_day, day_of_week, month
- **Binary Features (3)**: is_weekend, is_holiday, is_long_weekend

### Prediction Request Format
```json
{
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
  "current_demand": 2000.0,
  "actual_demand": null
}
```

## 🏗️ Project Structure

```
backend/
├── models/
│   ├── app.py              # FastAPI app for model inference
│   ├── predict.py          # Prediction functions
│   ├── model_utils.py      # Model utilities and data loading
│   ├── train_model.py      # Model training script
│   └── lgb_model.pkl       # Trained LightGBM model
├── api/
│   ├── holidays.py         # Holiday API endpoints
│   ├── weather.py          # Weather API endpoints
│   └── carbon.py           # Carbon intensity API endpoints
├── data/
│   └── electricity.csv     # Historical electricity data
├── main.py                 # Main FastAPI application
├── start_server.py         # Server startup script
├── test_model.py           # Model testing script
└── requirements.txt        # Python dependencies
```

## 🐛 Troubleshooting

### Common Issues

1. **LightGBM Import Error**
   ```bash
   pip install lightgbm
   ```

2. **Model Feature Mismatch**
   - Ensure the model is trained with the same features as defined in `model_utils.py`
   - Run `python models/train_model.py` to create a compatible model

3. **CSV Column Mismatch**
   - The CSV file columns are automatically mapped in `model_utils.py`
   - Ensure your CSV has the expected columns: datetime, Power demand, temp, dwpt, rhum, wdir, wspd, pres

4. **Memory Issues**
   - If you encounter memory errors, try reducing the data size or using a smaller model

### Testing
Run the test script to verify everything is working:
```bash
python test_model.py
```

## 📝 Notes

- The model uses a sample/dummy model for testing. For production, replace with a properly trained model.
- The API includes endpoints for weather, holidays, and carbon data that may require API keys.
- The prediction endpoint supports real-time updates through the `actual_demand` parameter.
