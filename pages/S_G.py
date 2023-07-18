import streamlit as st
import pandas as pd # for data analysis
import numpy as np # for numerical functions
import plotly.express as px #for interactive plots

@st.cache_data
def load_data():
    path = 'data\Station_GeoLocation_Longitute_Latitude_Elevation_EPSG_4326.csv'
    df = pd.read_csv(path)
    return df

with st.spinner('Loading Data..'):
    df = load_data()

st.title('Weather Data Analysis')

if st.checkbox('Show Dataset', True):
    st.subheader('Dataset')
    st.dataframe(df)