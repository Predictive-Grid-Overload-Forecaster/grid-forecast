#!/usr/bin/env python3
"""
Test script to demonstrate API validation requirements and common errors.
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8001"

def test_valid_request():
    """Test with a valid request format."""
    print("🧪 Testing VALID request format...")
    
    valid_data = {
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
        "current_demand": 2000.0,
        "actual_demand": None  # Optional
    }
    
    response = requests.post(f"{BASE_URL}/api/predict", json=valid_data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def test_invalid_requests():
    """Test various invalid request formats to show common validation errors."""
    print("🚨 Testing INVALID request formats...")
    
    # Test 1: Missing required field
    print("1. Missing required 'weather' field:")
    invalid_data1 = {
        "timestamp": datetime.now().isoformat(),
        "binary": {"is_weekend": 0, "is_holiday": 0, "is_long_weekend": 0},
        "categorical": {"quarter": 1, "hour_of_day": 14, "day_of_week": 1, "month": 1},
        "current_demand": 2000.0
    }
    response = requests.post(f"{BASE_URL}/api/predict", json=invalid_data1)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 2: Wrong data type
    print("2. Wrong data type (string instead of float):")
    invalid_data2 = {
        "timestamp": datetime.now().isoformat(),
        "weather": {
            "temp_c": "25.0",  # String instead of float
            "dewpoint_c": 20.0,
            "rel_humidity_pct": 60.0,
            "wind_dir_deg": 180.0,
            "wind_speed_ms": 5.0,
            "pressure_hpa": 1013.0
        },
        "binary": {"is_weekend": 0, "is_holiday": 0, "is_long_weekend": 0},
        "categorical": {"quarter": 1, "hour_of_day": 14, "day_of_week": 1, "month": 1},
        "current_demand": 2000.0
    }
    response = requests.post(f"{BASE_URL}/api/predict", json=invalid_data2)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()
    
    # Test 3: Invalid timestamp format
    print("3. Invalid timestamp format:")
    invalid_data3 = {
        "timestamp": "2024-01-01",  # Missing time part
        "weather": {
            "temp_c": 25.0,
            "dewpoint_c": 20.0,
            "rel_humidity_pct": 60.0,
            "wind_dir_deg": 180.0,
            "wind_speed_ms": 5.0,
            "pressure_hpa": 1013.0
        },
        "binary": {"is_weekend": 0, "is_holiday": 0, "is_long_weekend": 0},
        "categorical": {"quarter": 1, "hour_of_day": 14, "day_of_week": 1, "month": 1},
        "current_demand": 2000.0
    }
    response = requests.post(f"{BASE_URL}/api/predict", json=invalid_data3)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")
    print()

def show_correct_format():
    """Show the correct request format."""
    print("✅ CORRECT REQUEST FORMAT:")
    print("=" * 50)
    
    example = {
        "timestamp": "2024-01-01T14:30:00",  # ISO format datetime
        "weather": {
            "temp_c": 25.0,                 # Required: float
            "dewpoint_c": 20.0,             # Optional: float or null
            "rel_humidity_pct": 60.0,       # Optional: float or null
            "wind_dir_deg": 180.0,          # Optional: float or null
            "wind_speed_ms": 5.0,           # Optional: float or null
            "pressure_hpa": 1013.0          # Optional: float or null
        },
        "binary": {
            "is_weekend": 0,                # Required: int (0 or 1)
            "is_holiday": 0,                # Required: int (0 or 1)
            "is_long_weekend": 0            # Required: int (0 or 1)
        },
        "categorical": {
            "quarter": 1,                   # Required: int (1-4)
            "hour_of_day": 14,              # Required: int (0-23)
            "day_of_week": 1,               # Required: int (0-6, Monday=0)
            "month": 1                      # Required: int (1-12)
        },
        "current_demand": 2000.0,          # Optional: float (default: 0)
        "actual_demand": None               # Optional: float or null
    }
    
    print(json.dumps(example, indent=2))
    print()
    
    print("📝 FIELD REQUIREMENTS:")
    print("- timestamp: ISO format datetime string (e.g., '2024-01-01T14:30:00')")
    print("- weather.temp_c: Required float")
    print("- weather.*: All other weather fields are optional floats")
    print("- binary.*: All required integers (0 or 1)")
    print("- categorical.*: All required integers")
    print("- current_demand: Optional float (defaults to 0)")
    print("- actual_demand: Optional float (defaults to null)")

def main():
    print("🔍 API Validation Testing")
    print("=" * 50)
    
    # Test server connection
    try:
        response = requests.get(f"{BASE_URL}/ping")
        if response.status_code == 200:
            print("✅ Server is running")
        else:
            print("❌ Server is not responding properly")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure it's running on port 8001")
        return
    
    print()
    show_correct_format()
    print()
    test_valid_request()
    test_invalid_requests()

if __name__ == "__main__":
    main()
