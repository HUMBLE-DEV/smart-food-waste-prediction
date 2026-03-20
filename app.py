from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
from preprocessing import preprocess_features



app = Flask(__name__)
# Define the custom function again

model = joblib.load("company_food_waste_pipeline.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Keep categorical values as strings
        day = request.form['Day_of_Week']          # e.g. "Tuesday"
        weather = request.form['Weather']          # e.g. "Sunny"

        # Convert numeric values only
        expected_customers = int(request.form['Expected_Customers'])
        previous_day = int(request.form['Previous_Day_Consumption'])
        previous_week = int(request.form['Previous_Week_Same_Day'])
        festival = int(request.form['Festival'])      # e.g. "Yes" or "No"

        # Build DataFrame for pipeline
        new_data = pd.DataFrame([{
            'Day_of_Week': day,
            'Festival': festival,
            'Weather': weather,
            'Expected_Customers': expected_customers,
            'Previous_Day_Consumption': previous_day,
            'Previous_Week_Same_Day': previous_week
        }])

        # Predict
        prediction = model.predict(new_data)[0]

        return render_template('index.html', prediction_text=f"Predicted Meals Consumed: {int(prediction)}")
    except Exception as e:
        # Catch any unexpected errors and show a friendly message
        return render_template('index.html', prediction_text=f"Error: Please fill all fields correctly. ({e})")


if __name__ == "__main__":
    app.run(debug=True)
