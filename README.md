# Sugarcane Smart Irrigation AI 

## Overview
Sugarcane Smart Irrigation AI is a machine-learning-based academic prototype that predicts whether irrigation may be needed based on soil moisture, temperature, humidity, and rainfall.

The project demonstrates how environmental inputs can be used to generate an irrigation advisory through an interactive web application.

## Problem Statement
Irrigation decisions based only on experience may contribute to inefficient water use. This project demonstrates a software-based approach to supporting irrigation decisions using environmental data.

## Objectives
- Build a machine learning model for irrigation-need classification.
- Accept farm-condition inputs through an interactive dashboard.
- Display a prediction and model-estimated probability.
- Visualize the entered conditions and model feature importance.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Joblib
- Matplotlib
- Streamlit
- GitHub and Streamlit Community Cloud

## Input Features
- Soil moisture (%)
- Temperature (°C)
- Humidity (%)
- Rainfall (mm)

## Application Workflow
1. The user enters farm conditions using dashboard sliders.
2. The inputs are arranged into the feature format expected by the trained model.
3. The model predicts whether irrigation may be needed.
4. The application displays the prediction and, when supported, the model-estimated probability.
5. Charts help visualize the inputs and model feature importance.

## Limitations
This academic prototype uses synthetic demonstration data. Its predictions and probabilities have not been validated against real sugarcane field measurements. It should not be used as the sole basis for actual irrigation decisions.

## How to Run Locally
1. Clone or download this repository.
2. Install the dependencies listed in `requirements.txt`.
3. Ensure `sugarcane_irrigation_model.pkl` is in the same directory as `app.py`.
4. Run:

```bash
streamlit run app.py
```

## Future Improvements
- Train and evaluate the model using real agricultural datasets.
- Include crop growth stage and soil type.
- Integrate reliable weather forecasts and field sensor data.
- Validate recommendations with agricultural experts.

## Project Type
Academic machine learning prototype — Sugarcane Smart Irrigation AI.
