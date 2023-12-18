#import library
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
import tensorflow
from tensorflow import keras
import numpy as np
from PIL import Image
from flask import Flask, request, jsonify

#Load model
model = keras.models.load_model("model10.h5")
#label yang ada didalam model

label = ['angry','disgust','fear','happy','sad','surprise','neutral']
#label = ['Anger','Disgust','Fear','Happiness','Sadness','Surprise']

app = Flask(__name__)

#Function buat melakukan predict gambar input
def predict_label(img):
    i = np.asarray(img) / 255.0
    #sesuaikan input size yang dibuat dsaat bikin model
    i = i.reshape(1, 48, 48, 3)
    pred = model.predict(i)
    result = label[np.argmax(pred)]
    return result

@app.route("/predict", methods=["POST"])
def index():
    file = request.files.get('file')
    if file is None or file.filename == "":
        return jsonify({"error": "no file"})
    
    image_bytes = file.read()
    img = Image.open(io.BytesIO(image_bytes))
    img = img.resize((48,48), Image.NEAREST)
    pred_img = predict_label(img)
    return pred_img

if __name__ == "__main__":
    app.run(debug=True, port=3000)


