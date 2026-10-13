# Fire Detection AI

A computer vision web application that uses deep learning to classify uploaded images as fire or no fire.

## Overview

This project combines a Flask web application with a trained MobileNetV2-based neural network. Users can upload an image through a web interface and view the model's prediction.

## Features

- Image upload through a web interface
- Deep learning inference using TensorFlow and Keras
- MobileNetV2-based image classification model
- Displays the uploaded image and prediction result
- Simple browser-based interface built with HTML and CSS

## Technology Stack

- Python 3.11
- Flask
- TensorFlow / Keras
- NumPy
- Pillow
- HTML and CSS
- MobileNetV2

## Project Structure

```text
fire_detection_web/
├── app.py
├── fire_detection_model.keras
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── uploads/
```

## Installation

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd fire_detection_web
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with the URL of your repository.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## How It Works

1. The user uploads an image through the web interface.
2. The application resizes the image to 224 × 224 pixels.
3. The processed image is passed to the trained model.
4. The application displays the predicted class and the uploaded image.

## Model

The saved Keras model uses a MobileNetV2 feature extractor and a single-output classification layer.

The model file is included in the repository so the application can load it locally.

## Limitations

- Predictions depend on the quality and representativeness of the training data.
- Performance on unfamiliar environments may differ from performance on the training and validation datasets.
- Displayed percentages should not be interpreted as calibrated probabilities unless calibration has been evaluated.
- This project is an educational computer vision demonstration and is not a substitute for certified fire detection or alarm equipment.

## Future Improvements

- Evaluate performance on a separate test dataset.
- Report precision, recall, F1-score, and a confusion matrix.
- Improve file-upload validation and error handling.
- Add a more responsive user interface.
- Deploy the application for demonstration purposes.

## License

A license has not yet been selected. Please check the dataset and model's original terms before choosing a license for this repository.