import streamlit as st
import pandas as pd # for data analysis
import numpy as np # for numerical functions
import plotly.express as px #for interactive plots

@st.cache_data
def load_data():
    path = 'data\weather_Rourkela_2021_2022.csv'
    df = pd.read_csv(path,parse_dates=['time'])
    df['time'] = pd.to_datetime(df['time'], format='%d-%m-%Y')
    df.set_index('time', inplace=True)
    return df

with st.spinner('Loading Data..'):
    df = load_data()

st.title('Weather Data Analysis')

if st.checkbox('Show Dataset', True):
    st.subheader('Dataset')
    st.dataframe(df)
    st.sidebar.dataframe(df.dtypes)
    cols = st.multiselect("select columns to visualize", df.columns.tolist()) 
    col1, col2 = st.columns(2)
    graph = col1.radio('select a graph style', ['bar','area','line','scatter'])  
    choice = col2.radio('Select a time period', ['M','D','W','Y','2M','2W'])
    df = df.resample(choice).sum()
    for col in cols:
        try:
            if graph=='bar':fig = px.bar(df, x=df.index, y=col, title=f'{col} data graph')
            if graph=='area':fig = px.area(df, x=df.index, y=col, title=f'{col} data graph')
            if graph=='line':fig = px.line(df, x=df.index, y=col, title=f'{col} data graph')
            if graph=='scatter':fig = px.scatter(df, x=df.index, y=col, title=f'{col} data graph')
            st.plotly_chart(fig, use_container_width=True) 
        except:
            st.info('Please try again with different options')