import csv
import dataclasses
from altair import data_transformers
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import os




# Function to fetch real-time weather data from OpenWeatherMap API
def get_real_time_weather_data(api_key, city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can use "imperial" for Fahrenheit
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data
    else:
        st.error(f"Error: {data['message']}")
        return None



# Set page title and icon
st.set_page_config(page_title='Weather Data Visualization', page_icon=':partly_sunny:')

# Page header
st.title('Weather Data Visualization')

# Sidebar section for user input
st.sidebar.header('Options')
selected_metric = st.sidebar.selectbox('Select a metric:', ('Temperature (C)', 'Humidity (%)', 'Wind Speed (km/h)'))

# Add input field for the city name
city = st.sidebar.text_input('Enter your city:', 'New York')

# Get real-time weather data from OpenWeatherMap API
api_key = "6dcfd551b96e5d92259172d56ebaa143"  # Replace with your actual API key

# Check if the user has entered a city name
if city:
    real_time_data = get_real_time_weather_data(api_key, city)

    if real_time_data is not None:
        # Extract relevant weather information from the API response
        temperature = real_time_data["main"]["temp"]
        humidity = real_time_data["main"]["humidity"]
        wind_speed = real_time_data["wind"]["speed"]

        # Display real-time weather information
        st.subheader('Real-Time Weather Information')
        st.markdown(f'**City:** {city}')
        st.markdown(f'**Temperature (C):** {temperature}')
        st.markdown(f'**Humidity (%):** {humidity}')
        st.markdown(f'**Wind Speed (km/h):** {wind_speed}')




# Description section
st.subheader('About Weather Data Visualization')
st.markdown('''
This web application allows you to visualize weather data for different metrics over time. 
You can select the metric of interest from the sidebar dropdown menu, and the corresponding 
line chart will be displayed above. Additionally, you can enter your city in the input field 
to get real-time weather information for that city.

The data is read from CSV files located in the 'data' folder. Ensure that the folder contains 
CSV files with columns for Date, Temperature (C), Humidity (%), and Wind Speed (km/h). You can 
change the folder path in the function call to use a different folder containing your own 
weather data in the same format.

Feel free to explore and analyze the weather trends!
''')

