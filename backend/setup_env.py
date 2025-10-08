#!/usr/bin/env python3
"""
Setup script to help configure environment variables for the Grid Forecast API.
"""

import os
from pathlib import Path

def create_env_file():
    """Create a .env file with default values."""
    env_path = Path(__file__).parent / ".env"
    
    if env_path.exists():
        print("✅ .env file already exists")
        return
    
    print("🔧 Creating .env file...")
    
    env_content = """# Grid Forecast API Environment Variables
# Copy this file and update with your actual API keys

# Calendarific API (for holidays) - Get free key at: https://calendarific.com/
CALENDARIFIC_API_KEY=your_calendarific_api_key_here
COUNTRY=IN

# OpenWeather API (for weather data) - Get free key at: https://openweathermap.org/api
WEATHER_API_KEY=your_openweather_api_key_here

# Optional: Logging level
LOG_LEVEL=INFO
"""
    
    with open(env_path, 'w') as f:
        f.write(env_content)
    
    print("✅ Created .env file")
    print("📝 Please edit .env file and add your API keys")
    print("🔗 Get API keys from:")
    print("   - Calendarific: https://calendarific.com/")
    print("   - OpenWeather: https://openweathermap.org/api")

def check_env_vars():
    """Check which environment variables are set."""
    print("\n🔍 Checking environment variables...")
    
    required_vars = {
        "CALENDARIFIC_API_KEY": "Calendarific API key for holidays",
        "COUNTRY": "Country code (e.g., 'IN' for India)",
        "WEATHER_API_KEY": "OpenWeather API key for weather data"
    }
    
    missing_vars = []
    
    for var, description in required_vars.items():
        value = os.getenv(var)
        if value and value != f"your_{var.lower()}_here":
            print(f"✅ {var}: Set")
        else:
            print(f"❌ {var}: Not set - {description}")
            missing_vars.append(var)
    
    if missing_vars:
        print(f"\n⚠️  Missing environment variables: {', '.join(missing_vars)}")
        print("📝 Set them in your .env file or as system environment variables")
    else:
        print("\n🎉 All environment variables are configured!")

def main():
    print("🚀 Grid Forecast API Setup")
    print("=" * 40)
    
    create_env_file()
    check_env_vars()
    
    print("\n📖 Next steps:")
    print("1. Edit .env file with your API keys")
    print("2. Restart the server: python -m uvicorn backend.main:app --reload")
    print("3. Test the API endpoints")

if __name__ == "__main__":
    main()
