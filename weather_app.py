import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("WEATHER_API_KEY")

# Page config
st.set_page_config(page_title="Weather App", page_icon="🌦", layout="centered")

st.title("🌦 Weather App")
st.write("Get real-time weather information for any city.")

city = st.text_input("Enter City Name")

if st.button("Get Weather"):
    if not city:
        st.warning("Please enter a city name.")
    elif not api_key:
        st.error("API key not found. Check your .env file.")
    else:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                temp = data["main"]["temp"]
                humidity = data["main"]["humidity"]
                wind = data["wind"]["speed"]
                description = data["weather"][0]["description"].title()

                st.success(f"Weather in {city.title()}")

                st.metric("🌡 Temperature (°C)", temp)
                st.metric("💧 Humidity (%)", humidity)
                st.metric("🌬 Wind Speed (m/s)", wind)

                st.write(f"☁ Condition: **{description}**")

            else:
                st.error("City not found. Please check spelling.")

        except Exception as e:
            st.error("Something went wrong. Please try again.")