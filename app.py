
from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("forest_model.pkl")

# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Prediction
@app.route('/predict', methods=['POST'])
def predict():

    pm10 = float(request.form['pm10'])
    pm2_5 = float(request.form['pm2_5'])
    carbon_monoxide = float(request.form['carbon_monoxide'])
    nitrogen_dioxide = float(request.form['nitrogen_dioxide'])
    sulphur_dioxide = float(request.form['sulphur_dioxide'])
    ozone = float(request.form['ozone'])
    aerosol_optical_depth = float(request.form['aerosol_optical_depth'])
    dust = float(request.form['dust'])
    uv_index = float(request.form['uv_index'])

    # Create DataFrame with the same feature names
    features = pd.DataFrame([[
        pm10,
        pm2_5,
        carbon_monoxide,
        nitrogen_dioxide,
        sulphur_dioxide,
        ozone,
        aerosol_optical_depth,
        dust,
        uv_index
    ]], columns=[
        "pm10",
        "pm2_5",
        "carbon_monoxide",
        "nitrogen_dioxide",
        "sulphur_dioxide",
        "ozone",
        "aerosol_optical_depth",
        "dust",
        "uv_index"
    ])

    # Prediction
    prediction = model.predict(features)[0]

    if prediction == "Good":
        result = "Good"
    else:
        result = "Poor"

    return render_template(
        'index.html',
        prediction_text=f"The air quality is {result}"
    )


if __name__ == '__main__':
    app.run(debug=True)
