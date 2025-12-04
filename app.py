import streamlit as st
import requests
import time

st.set_page_config(page_title="ESP32 Live Dashboard", layout="centered")

ESP_URL = st.secrets["esp_url"]  # from secrets.toml

st.title("🌐 ESP32 Live Dashboard")
st.write("Real-time Temperature, Humidity & PWM LED Control")

# ---------------- PWM SLIDER ----------------
pwm_value = st.slider("LED Brightness (PWM 0–255)", 0, 255, 0)

if st.button("Set PWM"):
    try:
        r = requests.post(ESP_URL, data=f"led={pwm_value}")
        st.success(f"PWM set to {pwm_value}")
    except:
        st.error("Failed to send PWM to ESP32")

# ---------------- AUTO UPDATE SENSOR DATA ----------------
temp_placeholder = st.empty()
hum_placeholder = st.empty()

while True:
    try:
        r = requests.get(ESP_URL, timeout=2)
        data = r.json()

        temp_placeholder.write(f"🌡️ **Temperature:** {data['temperature']} °C")
        hum_placeholder.write(f"💧 **Humidity:** {data['humidity']} %")

    except:
        temp_placeholder.write("❌ Cannot reach ESP32")
        hum_placeholder.write("")

    time.sleep(1)
