import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import sklearn
import pyodbc


# @st.cache_resource
# def init_connection():
#     return pyodbc.connect(
#         "DRIVER={ODBC Driver 17 for SQL Server};SERVER=LAPTOP-NF09C5DT"
#         + st.secrets["server"]
#         + ";DATABASE=AirlineSatisfaction"
#         + st.secrets["database"]
#         + ";UID=SA"
#         + st.secrets["username"]
#         + ";PWD=cobac123456"
#         + st.secrets["password"]
#     )

# conn = init_connection()

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('Airline Quality Ratings.csv')
    return data

data = load_data()

# Title of the app
st.title("Airline Quality Ratings")

st.image('R.jpg')

# Apply the selected theme

st.page_link("Home_🏡.py", label="Home", icon="🏠")
st.page_link("pages/Data_📑.py", label="Data", icon="📚")
st.page_link("pages/Dashboard_📊.py", label="Dashboard", icon="1️⃣")
st.page_link("pages/Model_🤖.py", label="Model", icon="2️⃣")
st.page_link("http://www.google.com", label="Google", icon="🌎")


