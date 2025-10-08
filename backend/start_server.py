#!/usr/bin/env python3
"""
Startup script for the Grid Forecast API server.
"""

import uvicorn
from main import app

if __name__ == "__main__":
    print("🚀 Starting Grid Forecast API Server...")
    print("📊 Model inference ready")
    print("🌐 Server will be available at: http://localhost:8000")
    print("📖 API docs available at: http://localhost:8000/docs")
    print("=" * 50)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

