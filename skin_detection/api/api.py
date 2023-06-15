import pandas as pd
from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from skin_detection.interface.main import load_model, pred

app = FastAPI()
app.state.model = load_model()
app.state.image = None

# Allowing all middleware is optional, but good practice for dev purposes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# http://127.0.0.1:8000/predict?
@app.get("/predict")
def predict():
    """
    Make a single course prediction.
    """
    result = pred(model=app.state.model, image=app.state.image)[0][0]
    response = {
        'percentage': f'{result}'
        }
    return response

@app.get("/")
def root():
    response = {
        'greeting': 'Hello'
        }
    return response

@app.post("/upload-image")
async def upload_image(image: UploadFile = UploadFile(default=None)):
    file_content = await image.read()
    app.state.image = file_content

    return {"message": "Image uploaded successfully"}
