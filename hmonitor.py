import streamlit as st
import random
import time

st.title("Hospital sensor live monitoring ")

st.write("simulating live sensor data: heart rate,temperature, Oxygen level")

def sensor_data_stream():
    while True:
        yield{
            "heart_rate": random.randint(60, 100),
            "temperature": round(random.uniform(97.0, 100.0), 1),
            "oxygen_level": random.randint(90, 100)
        }
        time.sleep(1)  # simulate a realtime delay

#streamlit UI placeholders
heart_rate_bar = st.progress(0)
temperature_bar = st.progress(0)
oxygen_bar = st.progress(0)

heart_rate_text = st.empty()
temperature_text = st.empty()
oxygen_text = st.empty()

for reading in sensor_data_stream():
    hr = reading["heart_rate"]
    temp = reading["temperature"]
    ox = reading["oxygen_level"]

    #update progress bars(scale%)

    heart_rate_bar.progress(min(hr,100))
    temperature_bar.progress(min(int((temp-97)/3*100),100))  # scale temperature to 0-100%
    oxygen_bar.progress(ox)

    #update text display
    heart_rate_text.text(f"Heart Rate: {hr} bpm")
    temperature_text.text(f"Temperature: {temp} °F")
    oxygen_text.text(f"Oxygen Level: {ox} %")