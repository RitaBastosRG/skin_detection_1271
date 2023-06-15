# file for the functions
import sys
sys.path.append("..")

# package for image processing and display
from PIL import Image

# helper functions defined in the utils module
from utils import *

def load_model():
    return None

def preprocess_features(image: Image):
    image = square_image(image)
    radius = detect_black_coners(image)
    if radius> 0:
        image=remove_black_corners(image, radius=radius)
    return image

def pred(X_pred: Image ):
    """
    Make a prediction using the latest trained model
    """

    print("\n⭐️ Use case: predict")

    if X_pred is None:
        pass

    model = load_model()
    assert model is not None

    X_processed = preprocess_features(X_pred)
    y_pred = model.predict(X_processed)

    print("\n✅ prediction done: {} is your possibility of skin cancer \n")
    return y_pred

if __name__ == '__main__':
    pred()
