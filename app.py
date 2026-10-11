
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Sugarcane Smart Irrigation AI",
    page_icon="🌱",
    layout="wide"
)

@st.cache_resource
def load_model():
    return joblib.load("/content/sugarcane_irrigation_model.pkl")

model = load_model()

st.title("🌱 Sugarcane Smart Irrigation AI")
st.subheader("Machine Learning-Based Irrigation Advisory")
st.write(
    "An academic prototype that predicts whether irrigation may be needed "
    "from soil moisture, temperature, humidity and rainfall."
)

st.warning(
    "Prototype limitation: this model was trained on synthetic demonstration "
    "data. Predictions are not validated agricultural advice."
)

st.sidebar.header("Farm Conditions")

soil = st.sidebar.slider("Soil Moisture (%)", 10, 90, 25)
temperature = st.sidebar.slider("Temperature (°C)", 20, 42, 34)
humidity = st.sidebar.slider("Humidity (%)", 25, 95, 40)
rainfall = st.sidebar.slider("Rainfall (mm)", 0, 30, 2)

st.markdown("### Current Farm Inputs")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Soil Moisture", f"{soil}%")
c2.metric("Temperature", f"{temperature} °C")
c3.metric("Humidity", f"{humidity}%")
c4.metric("Rainfall", f"{rainfall} mm")

sample = pd.DataFrame([{
    "Soil_Moisture": soil,
    "Temperature": temperature,
    "Humidity": humidity,
    "Rainfall": rainfall
}])

if st.button("Generate Irrigation Advisory", type="primary"):
    prediction = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0][1]

    st.markdown("### AI Advisory")

    if prediction == 1:
        st.warning("The model predicts that irrigation may be needed.")
    else:
        st.success("The model predicts that irrigation may not be needed.")

    st.metric(
        "Model-estimated probability of irrigation needed",
        f"{probability * 100:.1f}%"
    )

    st.caption(
        "This probability reflects the demonstration model, not a calibrated "
        "estimate of actual crop water stress."
    )

st.markdown("### Farm Conditions Visualization")

fig, ax = plt.subplots()
ax.bar(
    ["Soil Moisture (%)", "Temperature (°C)", "Humidity (%)", "Rainfall (mm)"],
    [soil, temperature, humidity, rainfall]
)
ax.set_ylabel("Entered value")
ax.tick_params(axis="x", rotation=15)
fig.tight_layout()
st.pyplot(fig)

if hasattr(model, "feature_importances_"):
    st.markdown("### Model Feature Importance")
    importance = pd.DataFrame({
        "Feature": [
            "Soil Moisture", "Temperature", "Humidity", "Rainfall"
        ],
        "Importance": model.feature_importances_
    }).sort_values("Importance", ascending=False)

    st.bar_chart(importance.set_index("Feature"))

st.divider()
st.caption("Academic prototype | Sugarcane Smart Irrigation AI")
