# grid-forecast

Problem Statements:  
The Predictive Grid Overload Forecaster – Delhi Transco Ltd. needs to anticipate and manage demand spikes to prevent grid collapse during extreme weather. Your challenge is to build a high-fidelity energy demand forecasting model. Using historical hourly energy demand for public holidays and major city events, your AI must predict demand with pinpoint accuracy at a zonal level.

## File Structure

```text
grid-forecast/
│── backend/                
│   ├── main.py             # Entry point (FastAPI app)
│   ├── data/               # Kaggle datasets
│   │   ├── electricity.csv
│   │   ├── weather.csv
│   │   ├── holidays.csv
│   ├── core/
│   │   ├── config.py       # Environment variables, file paths
│   │   ├── cache.py        # Optional: caching preprocessed data
│   ├── models/
│   │   ├── train_model.py  # Training scripts
│   │   ├── predict.py      # Prediction scripts
│   ├── tests/
│   │   ├── test_preprocessing.py
│   │   ├── test_model.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example
│
│── frontend/               
│   ├── public/             # Static assets (logos, CSS, images)
│   ├── src/                
│   │   ├── App.js          # Main React / Next.js app
│   │   ├── components/     # Components: charts, tables, forms
│   │   ├── pages/          # For Next.js or routing
│   │   ├── services/       # Fetch predictions from backend
│   │   └── utils/          # Helper functions
│   ├── package.json
│
│── ai/                     
│   ├── notebooks/          
│   ├── pipelines/          
│   │   ├── query_assistant.py
│
│── assets/                 
│   ├── workflow.png
│   ├── ppt-template.pptx
│
│── docs/                   
│   ├── README.md
│   ├── API_REFERENCE.md
│
│── .gitignore

