
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Sugarcane Smart Irrigation AI",
    page_icon="🌱",
    layout="wide"
)

# --------------------------------------------------
# 2. LOAD THE SAVED MACHINE LEARNING MODEL
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "sugarcane_irrigation_model.pkl"


@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        st.error(
            "Model file not found. Make sure "
            "'sugarcane_irrigation_model.pkl' is uploaded "
            "to the root of your GitHub repository."
        )
        st.stop()

    return joblib.load(MODEL_PATH)


model = load_model()

# --------------------------------------------------
# 3. DASHBOARD HEADER
# --------------------------------------------------

st.title("🌱 Sugarcane Smart Irrigation AI")

st.subheader("Machine Learning-Based Irrigation Advisory")

st.write(
    "An academic prototype that predicts whether irrigation "
    "may be needed based on soil moisture, temperature, "
    "humidity, and rainfall."
)

st.warning(
    "Prototype limitation: This model was trained on synthetic "
    "demonstration data. Its predictions are not validated "
    "agricultural advice."
)

# --------------------------------------------------
# 4. FARM CONDITION INPUTS
# --------------------------------------------------

st.sidebar.header("Farm Conditions")

soil = st.sidebar.slider(
    "Soil Moisture (%)",
    min_value=10,
    max_value=90,
    value=25
)

temperature = st.sidebar.slider(
    "Temperature (°C)",
    min_value=20,
    max_value=42,
    value=34
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    min_value=25,
    max_value=95,
    value=40
)

rainfall = st.sidebar.slider(
    "Rainfall (mm)",
    min_value=0,
    max_value=30,
    value=2
)

# --------------------------------------------------
# 5. DISPLAY CURRENT INPUTS
# --------------------------------------------------

st.markdown("## Current Farm Inputs")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Soil Moisture", f"{soil}%")
c2.metric("Temperature", f"{temperature} °C")
c3.metric("Humidity", f"{humidity}%")
c4.metric("Rainfall", f"{rainfall} mm")

# --------------------------------------------------
# 6. PREPARE MODEL INPUT
# --------------------------------------------------

sample = pd.DataFrame(
    [{
        "Soil_Moisture": soil,
        "Temperature": temperature,
        "Humidity": humidity,
        "Rainfall": rainfall
    }],
    columns=[
        "Soil_Moisture",
        "Temperature",
        "Humidity",
        "Rainfall"
    ]
)

# --------------------------------------------------
# 7. GENERATE IRRIGATION ADVISORY
# --------------------------------------------------

st.markdown("## Irrigation Recommendation")

if st.button("Generate Irrigation Advisory", type="primary"):

    try:
        prediction = model.predict(sample)[0]

        st.markdown("### AI Advisory")

        if prediction == 1:
            st.warning(
                "The model predicts that irrigation may be needed."
            )
        else:
            st.success(
                "The model predicts that irrigation may not be needed."
            )

        # Display probability when supported by the model
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(sample)[0]

            classes = list(model.classes_)

            # Find the probability for class 1
            if 1 in classes:
                irrigation_index = classes.index(1)
                probability = probabilities[irrigation_index]

                st.metric(
                    "Model-estimated probability of irrigation needed",
                    f"{probability * 100:.1f}%"
                )
            else:
                st.info(
                    "The model does not contain a class labelled 1."
                )

        st.caption(
            "This probability comes from the demonstration model. "
            "It is not a calibrated estimate of actual crop water stress."
        )

    except Exception as error:
        st.error("Unable to generate the advisory.")
        st.exception(error)

# --------------------------------------------------
# 8. FARM CONDITIONS VISUALIZATION
# --------------------------------------------------

st.markdown("## Farm Conditions Visualization")

fig, ax = plt.subplots(figsize=(9, 4))

labels = [
    "Soil Moisture (%)",
    "Temperature (°C)",
    "Humidity (%)",
    "Rainfall (mm)"
]

values = [
    soil,
    temperature,
    humidity,
    rainfall
]

ax.bar(labels, values)

ax.set_ylabel("Entered value")
ax.set_title("Current Farm Conditions")
ax.tick_params(axis="x", rotation=15)

fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# --------------------------------------------------
# 9. MODEL FEATURE IMPORTANCE
# --------------------------------------------------

if hasattr(model, "feature_importances_"):

    st.markdown("## Model Feature Importance")

    feature_names = [
        "Soil Moisture",
        "Temperature",
        "Humidity",
        "Rainfall"
    ]

    importances = model.feature_importances_

    if len(importances) == len(feature_names):

        importance_df = pd.DataFrame({
            "Feature": feature_names,
            "Importance": importances
        }).sort_values(
            "Importance",
            ascending=False
        )

        st.bar_chart(
            importance_df.set_index("Feature")
        )

    else:
        st.info(
            "The number of model features differs from "
            "the four displayed input features."
        )

# --------------------------------------------------
# 10. FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Academic Prototype | Sugarcane Smart Irrigation AI"
)
