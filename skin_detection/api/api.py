import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from skin_detection_1271.interface.main import load_model

app = FastAPI()
app.state.model = load_model()

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
@app.get("/predict")
def predict(
    ):      # 1
    """
    Make a single course prediction.
    """
    X_pred=None
    y_pred = app.state.model.predict(preprocess_features(X_pred))[0][0]

    response = {
        'fare_amount': float(y_pred)
        }
    return response

@app.get("/")
def root():
    response = {
        'greeting': 'Hello'
        }
    return response
