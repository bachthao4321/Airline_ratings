import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt
import pickle
import sklearn

st.set_page_config(page_title="Dashboard", page_icon="📈")
# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('Airline Quality Ratings.csv')
    return data

data = load_data()


# Filter and display data by customer type
# st.subheader("Filter by Customer Type and Gender")
# customer_types = data['Customer Type'].unique()
# selected_customer_type = st.selectbox("Select a Customer Type", customer_types)
# genders = data['Gender'].unique()
# selected_gender = st.selectbox("Select Gender", genders)
# filtered_data = data[(data['Customer Type'] == selected_customer_type) & (data['Gender'] == selected_gender)]
# st.dataframe(filtered_data)

# Display summary of filtered data
# st.subheader(f"Summary of {selected_customer_type} and {selected_gender}")
# st.write(filtered_data.describe())

# Add Altair charts
st.title("Visualizations")

# Age Distribution
st.subheader("Age Distribution")
age_chart = alt.Chart(data).mark_bar().encode(
    alt.X("Age", bin=True),
    y='count()'
).properties(
    width=600,
    height=400
)
st.altair_chart(age_chart, use_container_width=True)


st.subheader("Rating of Services")
services = [
    'Departure and Arrival Time Convenience',
    'Ease of Online Booking',
    'Check-in Service',
    'Online Boarding',
    'Gate Location',
    'On-board Service',
    'Seat Comfort',
    'Leg Room Service',
    'Cleanliness',
    'Food and Drink',
    'In-flight Service',
    'In-flight Wifi Service',
    'In-flight Entertainment',
    'Baggage Handling'
]
selected_service_type = st.selectbox("Select a Service", services)
count_ratings = data[selected_service_type].value_counts().sort_index()

# Create a bar chart
st.bar_chart(count_ratings)



#Satisfaction by Gender, Class, Type of travel, Customer type
st.write("### Satisfaction by Categorical Values")
selected_value = st.radio("Select options",['Gender','Class','Type of Travel','Customer Type'])
selected_value_type = data[selected_value].unique()

satisfaction_categorical_chart = alt.Chart(data).mark_bar().encode(
    x=selected_value,
    y='count()',
    color='Satisfaction'
).properties(
    width=600,
    height=400
)
st.altair_chart(satisfaction_categorical_chart, use_container_width=True)

# Departure Delay vs. Arrival Delay
st.write("### Departure Delay vs. Arrival Delay")
delay_chart = alt.Chart(data).mark_point().encode(
    x='Departure Delay',
    y='Arrival Delay',
    color='Satisfaction',
    tooltip=['ID', 'Departure Delay', 'Arrival Delay', 'Satisfaction']
).properties(
    width=600,
    height=400
)
st.altair_chart(delay_chart, use_container_width=True)

# Flight Distance Distribution
st.write("### Flight Distance Distribution")
selected_value_flight = st.radio("Select options for flight distance",['Gender','Class','Type of Travel','Customer Type'])
distance_chart = alt.Chart(data).mark_bar().encode(
    alt.X("Flight Distance", bin=True),
    y='count()',
    color =selected_value_flight
).properties(
    width=600,
    height=400
)
st.altair_chart(distance_chart, use_container_width=True)

# Correlation Heatmap
st.write("### Correlation Heatmap")

# Correlation Heatmap
numeric_data = data.select_dtypes(include=['float64', 'int64'])
fig, ax = plt.subplots(figsize=(10, 8))  # Create a figure and axis
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)  # Plot heatmap on the axis
st.pyplot(fig)  # Display the figure using st.pyplot()


