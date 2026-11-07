# 🌿 AirSense AI – Air Quality Prediction System

AirSense AI is a machine learning-powered web application designed to predict air quality using environmental and atmospheric measurements. Built with Python, Flask, and a trained Random Forest classification model, the application analyzes nine environmental parameters to classify air quality as **Good** or **Poor**.

Users can enter pollutant concentrations and environmental indicators through a responsive web interface and receive an instant machine learning prediction.

### 🚀 Key Features
- Air quality classification using a trained Random Forest model.
- Prediction based on nine environmental parameters.
- Interactive and responsive web dashboard.
- Real-time predictions through a Flask backend.
- User-friendly environmental measurement form.
- Air quality reference information.
- Pre-trained model integration using Joblib.

### 🧠 Machine Learning Model
The application uses a Random Forest Classifier with nine input features:

1. PM10
2. PM2.5
3. Carbon Monoxide (CO)
4. Nitrogen Dioxide (NO₂)
5. Sulphur Dioxide (SO₂)
6. Ozone (O₃)
7. Aerosol Optical Depth (AOD)
8. Dust
9. UV Index

**Prediction Classes:**
- Good
- Poor

### 🛠️ Tech Stack
- **Programming Language:** Python
- **Machine Learning:** Scikit-learn, Random Forest
- **Backend:** Flask
- **Data Processing:** Pandas
- **Model Serialization:** Joblib
- **Frontend:** HTML5, CSS3, JavaScript
- **UI Design:** Responsive Dashboard

### 📂 Project Structure
```text
AirSense-AI/
│
├── app.py
├── forest_model.pkl
├── templates/
│   └── index.html
├── requirements.txt
└── README.md
```

### ⚙️ Installation & Setup
```bash
git clone YOUR_REPOSITORY_URL
cd AirSense-AI

pip install flask pandas joblib scikit-learn

python app.py
```

Open your browser:
```text
http://127.0.0.1:5000
```

### 🎯 Project Objective
The objective of AirSense AI is to demonstrate how machine learning can be integrated into a web application to analyze environmental data and provide accessible air quality predictions.

**Note:** Predictions depend on the training data and model. This project is an educational machine learning application, not a certified air quality monitoring or public health assessment system.

### 👨‍💻 Author
Developed as an AI/ML and Full-Stack Machine Learning project.

**Areas:** Artificial Intelligence | Machine Learning | Environmental Analytics | Flask Development
