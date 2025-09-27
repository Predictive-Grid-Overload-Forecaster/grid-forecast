# grid-forecast

Problem Statements:
The Predictive Grid Overload Forecaster The Delhi Transco Ltd. needs to anticipate and manage demand spikes to prevent grid collapse during extreme weather. Your challenge is to build a high-fidelity energy demand forecasting model. Using historical hourly energy demand for public holidays and major city events, your AI must predict demand with pinpoint accuracy at a zonal level.


# File Structure should look exactly like this: 
```
grid-forecast/
│── backend/                # FastAPI backend
│   ├── main.py              # Entry point
│   ├── api/                 # All API routes
│   │   ├── holidays.py
│   │   ├── weather.py
│   │   ├── carbon.py
│   ├── core/                # Core config & utilities
│   │   ├── config.py        # Environment variables, API keys
│   │   ├── cache.py         # Caching logic
│   ├── tests/               # Unit & integration tests
│   │   ├── test_holidays.py
│   │   ├── test_weather.py
│   │   ├── test_carbon.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .env.example         # Example env file (no secrets)

│── frontend/                # Optional (if you add UI later)
│   ├── public/              # Static assets (logos, images, CSS)
│   ├── src/                 # React / Next.js / Streamlit code
│   │   ├── App.js / index.js
│   ├── package.json

│── ai/                      # AI / LangChain experiments
│   ├── notebooks/           # Jupyter/Colab notebooks for prototyping
│   ├── pipelines/           # Scripts for chaining APIs / AI models
│   │   ├── query_assistant.py

│── assets/                  # Images, diagrams, ppt templates
│   ├── workflow.png
│   ├── ppt-template.pptx

│── docs/                    # Docs for presentation + reference
│   ├── README.md
│   ├── API_REFERENCE.md

│── .gitignore
```
