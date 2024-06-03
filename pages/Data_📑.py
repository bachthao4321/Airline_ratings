import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import sklearn

st.set_page_config(page_title="Data", page_icon="📚")
# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('Airline Quality Ratings.csv')
    return data

data = load_data()

satisfaction_count = data['Satisfaction'].value_counts()
satisfied_count = satisfaction_count.get('Neutral or Dissatisfied', 0)
dissatisfied_count = satisfaction_count.get('Satisfied', 0)

st.markdown(
    """
    <style>
    div[data-testid="stMetricLabel"] {
        background-color: #f0f2f6;
        border: 2px solid #d3d3d3;
        border-radius: 5px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Display the dataset
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Dataset")
with col2:
    st.metric("Total samples", len(data))
with col3:
    st.metric("Satisfied", satisfied_count)
with col4:
    st.metric("Dissatisfied", dissatisfied_count)

st.dataframe(data)

# Summary statistics
st.subheader("Summary Statistics")
st.write(data.describe())