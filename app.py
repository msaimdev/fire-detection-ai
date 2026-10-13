from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ensure folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# load model
model = tf.keras.models.load_model('fire_detection_model.keras')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():

    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # save image
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # preprocess image
    img = image.load_img(filepath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # prediction
    prediction = model.predict(img_array)[0][0]

    # FIXED LOGIC (your model is inverted)
    fire_prob = (1 - prediction) * 100
    no_fire_prob = prediction * 100

    # decision
    if prediction < 0.5:
        result = "🔥 FIRE DETECTED"
        badge = "danger"
    else:
        result = "🟢 NO FIRE"
        badge = "safe"

    return render_template(
        'index.html',
        prediction=result,
        fire_prob=fire_prob,
        no_fire_prob=no_fire_prob,
        badge=badge,
        image_path=filepath
    )


if __name__ == '__main__':
    app.run(debug=True)