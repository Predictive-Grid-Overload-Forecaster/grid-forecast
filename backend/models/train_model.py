"""
Training script for LightGBM model for electricity demand forecasting.
This is a placeholder - the actual model training should be done in the notebook.
"""

import pandas as pd
import numpy as np
from pathlib import Path
import joblib
from datetime import datetime

def create_sample_model():
    """
    Create a sample LightGBM model for testing purposes.
    In production, this should be replaced with proper model training.
    """
    try:
        import lightgbm as lgb
    except ImportError:
        print("LightGBM not installed. Please install it first: pip install lightgbm")
        return None
    
    # Create a simple dummy model for testing
    # In real implementation, this would be trained on actual data
    model = lgb.LGBMRegressor(
        objective='regression',
        n_estimators=100,
        learning_rate=0.1,
        max_depth=6,
        random_state=42
    )
    
    # Create dummy training data (this is just for testing)
    np.random.seed(42)
    n_samples = 1000
    n_features = 23  # matches the total number of features (16 numeric + 4 categorical + 3 binary)
    
    X_dummy = np.random.randn(n_samples, n_features)
    y_dummy = np.random.randn(n_samples) * 1000 + 2000  # realistic demand range
    
    # Train the dummy model
    model.fit(X_dummy, y_dummy)
    
    # Save the model
    model_path = Path(__file__).parent / "lgb_model.pkl"
    joblib.dump(model, model_path)
    print(f"Sample model saved to {model_path}")
    
    return model

if __name__ == "__main__":
    print("Creating sample LightGBM model...")
    model = create_sample_model()
    if model:
        print("Sample model created successfully!")
    else:
        print("Failed to create model. Please check LightGBM installation.")
