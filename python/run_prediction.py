import streamlit as st
import pandas as pd
import requests
import joblib
import time

# ============== CONFIG =================
ESP32_URL = "http://192.168.4.1/data"
REFRESH_TIME = 7  # seconds
# ======================================

st.set_page_config(
    page_title="Water Health Monitoring",
    layout="centered"
)

st.title("💧 Community Water Health Monitoring Dashboard")
st.caption("Early warning system for water-borne disease risk")

# Load ML model
model = joblib.load("model.pkl")

placeholder = st.empty()

def rule_based_status(d):
    if d["tds"] > 700 or d["turbidity"] > 5 or d["ph"] < 6 or d["ph"] > 8.5:
        return "POLLUTED", "🔴 High Risk"
    elif d["tds"] > 300 or d["turbidity"] > 2:
        return "MODERATE", "🟠 Monitor Closely"
    else:
        return "SAFE", "🟢 Drinkable"

while True:
    try:
        data = requests.get(ESP32_URL, timeout=3).json()

        df = pd.DataFrame(
            [[data["ph"], data["turbidity"], data["temperature"], data["tds"]]],
            columns=["ph", "turbidity", "temp", "tds"]
        )

        ml_pred = model.predict(df)[0]
        ml_label = ["SAFE", "MODERATE RISK", "HIGH RISK"][ml_pred]

        rule_label, rule_msg = rule_based_status(data)

        with placeholder.container():
            st.subheader("📊 Live Sensor Readings")

            c1, c2 = st.columns(2)
            c1.metric("pH", data["ph"])
            c2.metric("Temperature (°C)", data["temperature"])

            c3, c4 = st.columns(2)
            c3.metric("TDS (ppm)", data["tds"])
            c4.metric("Turbidity (NTU)", data["turbidity"])

            st.divider()

            st.subheader("🧪 Pollution Assessment")
            st.write(f"**Rule-Based Status:** {rule_label}")
            st.write(f"**Risk Level:** {rule_msg}")

            st.divider()

            st.subheader("🤖 ML-Based Prediction")
            st.success(f"Random Forest Result: **{ml_label}**")

            st.caption("Data refreshes automatically")

    except:
        st.error("Unable to connect to ESP32 node")

    time.sleep(REFRESH_TIME)
