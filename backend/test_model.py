#!/usr/bin/env python3
"""
Test script to verify the model inference functionality.
Run this script to test if all components are working correctly.
"""

import sys
from datetime import datetime
import requests
import json

def test_model_imports():
    """Test if all model components can be imported."""
    print("Testing model imports...")
    try:
        from models.model_utils import model, compute_lags_and_roll, update_recent_demand
        from models.predict import predict
        print("✅ Model imports successful")
        return True
    except Exception as e:
        print(f"❌ Model import failed: {e}")
        return False

def test_prediction():
    """Test the prediction functionality."""
    print("\nTesting prediction functionality...")
    try:
        from models.predict import predict
        
        # Test data
        timestamp = datetime.now()
        weather = {
            'temp_c': 25.0,
            'dewpoint_c': 20.0,
            'rel_humidity_pct': 60.0,
            'wind_dir_deg': 180.0,
            'wind_speed_ms': 5.0,
            'pressure_hpa': 1013.0
        }
        binary = {
            'is_weekend': 0,
            'is_holiday': 0,
            'is_long_weekend': 0
        }
        categorical = {
            'quarter': 1,
            'hour_of_day': 14,
            'day_of_week': 1,
            'month': 1
        }
        current_demand = 2000.0
        
        result = predict(timestamp, weather, binary, categorical, current_demand)
        print(f"✅ Prediction successful: {result} MW")
        return True
    except Exception as e:
        print(f"❌ Prediction failed: {e}")
        return False

def test_app_import():
    """Test if the FastAPI app can be imported."""
    print("\nTesting FastAPI app import...")
    try:
        from main import app
        print("✅ FastAPI app import successful")
        return True
    except Exception as e:
        print(f"❌ FastAPI app import failed: {e}")
        return False

def test_api_endpoint():
    """Test the API endpoint (if server is running)."""
    print("\nTesting API endpoint...")
    try:
        # Test data for API call
        test_data = {
            "timestamp": datetime.now().isoformat(),
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
        }
        
        response = requests.post(
            "http://localhost:8000/api/predict",
            json=test_data,
            timeout=5
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ API endpoint test successful: {result}")
            return True
        else:
            print(f"❌ API endpoint test failed: Status {response.status_code}, Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("⚠️  Server not running - start with: uvicorn main:app --host 0.0.0.0 --port 8000")
        return False
    except Exception as e:
        print(f"❌ API endpoint test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("🧪 Testing Grid Forecast Model Inference")
    print("=" * 50)
    
    tests = [
        test_model_imports,
        test_prediction,
        test_app_import,
        test_api_endpoint
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 50)
    print("📊 Test Summary:")
    print(f"✅ Passed: {sum(results)}/{len(results)}")
    print(f"❌ Failed: {len(results) - sum(results)}/{len(results)}")
    
    if all(results):
        print("\n🎉 All tests passed! Your model inference is ready to use.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
