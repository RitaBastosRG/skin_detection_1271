# file for the functions
# import sys
# sys.path.append("..")


from PIL import Image
from utils import *
from tensorflow import keras

MODEL_NAME = 'model_dummy'

def get_dummy_image()->Image:
    image_file_name='raw_data/SCC/ISIC_0024329.jpg'
    image = Image.open(image_file_name)
    return image

def load_model():
    model_file_name = f'skin_detection/model/{MODEL_NAME}'

    model = keras.models.load_model(model_file_name)

    return model

def preprocess_features(image: Image):

    image = square_image(image)
    radius = detect_black_coners(image)
    if radius> 0:
        image=remove_black_corners(image, radius=radius)
    return image

def pred(image=None):
    """
    Make a prediction using the latest trained model
    """
    if image is None:
        image = get_dummy_image()

    image = preprocess_features(image)
    image = image.resize((400,400),resample=Image.BILINEAR)
    X_pred = np.asarray(image, dtype=np.float32)
    X_pred = np.expand_dims(X_pred, axis=0)
    model = load_model()
    assert model is not None

    y_pred = model.predict(X_pred)
    for y in y_pred:
        p=y[0]
        if p<0.5:
            print(f"\n✅ your possibility of skin cancer is {np.round(p*100, 2)}% ✅\n")
        if p>0.5:
            print(f"\n❌ {np.round(p*100, 2)}% chance of cancer. You are screwed ❌\n")
    return y_pred

if __name__ == '__main__':
    import os

    current_path = os.getcwd()
    print("Current path:", current_path)

    pred()

    # image_file_name='raw_data/SCC/ISIC_0024329.jpg'
    # image = Image.open(image_file_name)
    # plt.imshow(image)
    # plt.show()
    # print(image.size)
    # image = preprocess_features(image)
    # print (image.size)
    # image = image.resize((400,400),resample=Image.BILINEAR)
    # print (image.size)
    # X_pred = np.asarray(image, dtype=np.float32)
    # print(X_pred.shape)
    # X_pred = np.expand_dims(X_pred, axis=0)
    # print(X_pred.shape)
