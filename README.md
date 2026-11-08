# AirSense AI — Random Forest Air-Quality Classification

AirSense AI is a Flask web application that uses a trained Random Forest classifier to categorize environmental measurements into **Good** or **Poor** air-quality classes.

The application accepts nine input parameters through a responsive form and returns the model's predicted class.

## Features

- Random Forest classification.
- Nine environmental input parameters.
- Flask prediction backend.
- Responsive web interface.
- Pre-trained model integration with Joblib.
- Good/Poor output labels.

## Input features

1. PM10
2. PM2.5
3. Carbon Monoxide (CO)
4. Nitrogen Dioxide (NO₂)
5. Sulphur Dioxide (SO₂)
6. Ozone (O₃)
7. Aerosol Optical Depth (AOD)
8. Dust
9. UV Index

## Technology

| Area | Technology |
|---|---|
| Language | Python |
| Machine learning | scikit-learn, Random Forest |
| Backend | Flask |
| Data processing | pandas |
| Model persistence | Joblib |
| Frontend | HTML, CSS, JavaScript |

## Project structure

```text
AirSense-AI/
├── app.py
├── forest_model.pkl
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone https://github.com/malikahmad/AirSense-AI-Air-Quality-Prediction-Using-Random-Forest-Flask.git
cd AirSense-AI-Air-Quality-Prediction-Using-Random-Forest-Flask

python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If the repository's requirements file is unavailable or incomplete, install the dependencies used by the application: Flask, pandas, Joblib, and scikit-learn.

## Run

```bash
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Evaluation recommendations

Before publishing performance claims, document the dataset source, feature units, preprocessing steps, train/test split, class balance, and model version. Report per-class precision, recall, F1-score, confusion matrix, and results on an untouched test set.

## Limitations

- Output depends on the training data and the feature definitions used during model development.
- The Good/Poor categories are model labels, not official regulatory air-quality categories.
- User-entered measurements may be inaccurate or use incompatible units.
- This application is an educational machine-learning demonstration, not a certified air-quality monitoring or public-health assessment system.

## Author

**Ahmad Zulfiqar** — [GitHub](https://github.com/malikahmad) · [LinkedIn](https://www.linkedin.com/in/malik-ahmad-06abb31a1/)
