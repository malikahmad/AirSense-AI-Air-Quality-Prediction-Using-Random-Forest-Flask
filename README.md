# AirSense AI

**Air quality classification with Random Forest, Flask, and environmental measurements.**

AirSense AI is a small machine-learning web application that accepts nine environmental inputs and uses a trained Random Forest classifier to return one of two labels: **Good** or **Poor**. The Flask application loads a serialized model with Joblib and presents the prediction in a browser interface.

> **Scope:** This is an educational machine-learning demonstration. It is not a regulatory air-quality monitor, a calibrated sensor, or a public-health assessment tool. Predictions depend on the model's training data, feature definitions, units, and preprocessing.

## Features

- Random Forest classification through a Flask web application.
- Nine environmental input variables.
- Browser-based input form and prediction result.
- Pre-trained model loaded from forest_model.pkl.
- Pandas DataFrame construction using the feature names expected by the application.

## Input features

The current app.py expects these nine fields, in this order:

| Feature | Form field / model column |
|---|---|
| PM10 | pm10 |
| PM2.5 | pm2_5 |
| Carbon monoxide | carbon_monoxide |
| Nitrogen dioxide | nitrogen_dioxide |
| Sulphur dioxide | sulphur_dioxide |
| Ozone | ozone |
| Aerosol optical depth | aerosol_optical_depth |
| Dust | dust |
| UV index | uv_index |

The application maps the model output to Good and Poor. Use the same units, column order, and feature preprocessing as the training pipeline that produced the model file.

## Technology

| Layer | Technology |
|---|---|
| Language | Python |
| Web backend | Flask |
| Machine learning | scikit-learn, Random Forest |
| Tabular input | pandas |
| Model loading | Joblib |
| Frontend | HTML, CSS, JavaScript |

## Project structure

~~~text
AirSense-AI/
├── app.py
├── forest_model.pkl
├── templates/
│   └── index.html
└── README.md
~~~

The repository currently does not include a requirements.txt. Install the dependencies listed below, or add a pinned dependency file after confirming the versions used to train and serialize the model.

## Getting started

### 1. Clone the repository

~~~bash
git clone https://github.com/malikahmad/AirSense-AI-Air-Quality-Prediction-Using-Random-Forest-Flask.git
cd AirSense-AI-Air-Quality-Prediction-Using-Random-Forest-Flask
~~~

### 2. Create a virtual environment

**Windows PowerShell**

~~~powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
~~~

**Linux / macOS**

~~~bash
python3 -m venv .venv
source .venv/bin/activate
~~~

### 3. Install dependencies

~~~bash
python -m pip install --upgrade pip
pip install Flask pandas joblib scikit-learn
~~~

For reproducible results, use the scikit-learn version compatible with the version that created forest_model.pkl. Loading a pickle/joblib model with a different scikit-learn version can produce warnings or errors.

### 4. Verify required files

Before running the application, confirm that both files exist:

- forest_model.pkl in the project root.
- templates/index.html in the templates directory.

The model file must be the trusted artifact created by this project's training process. Never load a Joblib/pickle file from an untrusted source.

### 5. Run locally

~~~bash
python app.py
~~~

Open http://127.0.0.1:5000 in your browser.

The current application starts Flask with debug mode enabled for local development. Do not use the development server or debug mode for a public production deployment. Configure a production WSGI server and disable debug mode before deployment.

## How prediction works

1. A user enters the nine environmental measurements in the web form.
2. Flask reads the submitted values and converts them to floating-point numbers.
3. The backend creates a one-row Pandas DataFrame with the expected feature names and order.
4. The loaded Random Forest model predicts a class.
5. The result is rendered on the web page as Good or Poor.

## Model and evaluation

The repository contains the serialized model artifact, but this README does not claim a specific accuracy or benchmark. For a meaningful evaluation, document:

- Dataset source, license, date range, and geographic coverage.
- Measurement units and missing-value handling.
- Train/validation/test split strategy.
- Class distribution and any class weighting or resampling.
- Accuracy, precision, recall, F1-score, and confusion matrix on an untouched test set.
- Scikit-learn and Python versions used for training.

Do not interpret the binary class output as an official AQI category unless the model has been trained and validated against the relevant AQI definition and thresholds.

## Troubleshooting

**Model file not found**
- Confirm forest_model.pkl is in the same directory as app.py.
- Run the command from the repository root.

**Template not found**
- Confirm the HTML file is located at templates/index.html.

**Model loading error**
- Install a scikit-learn version compatible with the training environment.
- Only load model files from a trusted source.

**Unexpected predictions**
- Verify the units and order of the nine input features.
- Confirm that the form field names match the backend.
- Compare preprocessing with the original training pipeline.

## Future improvements

- Add a pinned requirements.txt and automated setup checks.
- Validate missing, non-numeric, and out-of-range form values.
- Add a documented training/evaluation pipeline.
- Display the model version and input units in the interface.
- Add tests for the prediction route and feature ordering.
- Deploy with a production WSGI server and environment-based configuration.

## Author

**Ahmad Zulfiqar**  
GitHub: [@malikahmad](https://github.com/malikahmad)
