import streamlit as st
import requests
import time

st.set_page_config(page_title="ESP32 Live Dashboard", layout="centered")

st.title("🌐 ESP32 Live Dashboard")
st.write("Real-time Temperature, Humidity & LED Control")

ESP_URL = st.secrets["esp_url"]  # Your ESP32 API endpoint

# ---- LED CONTROL ----
st.subheader("LED Control")
col1, col2 = st.columns(2)

with col1:
    if st.button("Turn LED ON"):
        try:
            requests.get(ESP_URL + "/on")
            st.success("LED turned ON!")
        except:
            st.error("ESP unreachable")

with col2:
    if st.button("Turn LED OFF"):
        try:
            requests.get(ESP_URL + "/off")
            st.success("LED turned OFF!")
        except:
            st.error("ESP unreachable")

# ---- LIVE SENSOR DATA ----
st.subheader("Live Temperature & Humidity")

placeholder = st.empty()

while True:
    try:
        data = requests.get(ESP_URL + "/temp").json()
        temp = data["temperature"]
        hum = data["humidity"]

        with placeholder.container():
            st.metric("Temperature (°C)", temp)
            st.metric("Humidity (%)", hum)

    except:
        with placeholder.container():
            st.error("ESP32 Not reachable")

    time.sleep(2)
