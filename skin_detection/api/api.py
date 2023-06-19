import pandas as pd
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from skin_detection.interface.main import load_model, get_dummy_image,pred
from PIL import Image
import io

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

# http://127.0.0.1:8000/predict
@app.get("/predict")
def predict(
    ):      # 1
    """
    Make a single course prediction.
    """
    image=get_dummy_image()
    y_pred = pred(image)[0][0]

    response = {
        'possibility': float(y_pred)
        }
    return response

# http://127.0.0.1:8000
@app.get("/")
def root():
    response = {
        'greeting': 'Welcome to Skin Detection Website'
        }
    return response

"http://localhost:8000/upload-image/"
@app.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # image=get_dummy_image()
    y_pred = pred(image)[0][0]

    response = {
        "filename": file.filename,
        'possibility': float(y_pred)
        }
    return response
