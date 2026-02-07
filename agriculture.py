import streamlit as st
import random
import time
import pandas as pd

st.title("Smart Agriculture Monitoring System")

soil = random.randint(20, 80)
temp = random.randint(20, 40)
humidity = random.randint(40, 90)

pump_status = "ON" if soil < 40 else "OFF"

st.metric("Soil Moisture (%)", soil)
st.metric("Temperature (°C)", temp)
st.metric("Humidity (%)", humidity)
st.metric("Water Pump Status", pump_status)

data = {
    "Soil Moisture": [random.randint(20,80) for _ in range(10)],
    "Temperature": [random.randint(20,40) for _ in range(10)],
    "Humidity": [random.randint(40,90) for _ in range(10)]
}

df = pd.DataFrame(data)

st.line_chart(df)
