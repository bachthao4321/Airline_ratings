import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import sklearn

st.set_page_config(page_title="Model", page_icon="🚀")

# Load the dataset
@st.cache_data
def load_data():
    data = pd.read_csv('Airline Quality Ratings.csv')
    return data

data = load_data()

# Apply custom CSS to enhance the appearance
st.markdown("""
    <style>
    .stButton button {
        background-color: #33bbff;
        color: white;
        padding: 10px 24px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #33bbff;
    }
    .stNumberInput, .stSelectbox, .stSlider {
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.subheader("User Feedback Form")

# Create columns for layout
col1, col2 = st.columns(2)

with col1:
    # Select age
    age = st.number_input("Age", min_value=1, key='age_input')
    
    # Select Gender
    gender = st.selectbox("Gender", options=["Male", "Female"], key='gender_selectbox')

    # Select Customer Type
    customer_type = st.selectbox("Customer Type", options=data['Customer Type'].unique(), key='customer_type_selectbox')

    # Select Type of Travel
    type_of_travel = st.selectbox("Type of Travel", options=data['Type of Travel'].unique(), key='type_of_travel_selectbox')

    # Select Class
    travel_class = st.selectbox("Class", options=data['Class'].unique(), key='class_selectbox')

with col2:
    # Input Flight Distance
    flight_distance = st.number_input("Flight Distance", min_value=0, key='flight_distance_input')

    # Input Departure Delay
    departure_delay = st.number_input("Departure Delay", min_value=0, key='departure_delay_input')

    # Input Arrival Delay
    arrival_delay = st.number_input("Arrival Delay", min_value=0, key='arrival_delay_input')

# Create columns for layout
col3, col4 = st.columns(2)

with col3:
    # Ratings (1-5)
    def rating(label, key):
        return st.slider(label, min_value=1, max_value=5, step=1, key=key)

    departure_arrival_time_convenience = rating("Departure and Arrival Time Convenience", 'departure_arrival_time_convenience')
    ease_of_online_booking = rating("Ease of Online Booking", 'ease_of_online_booking')
    check_in_service = rating("Check-in Service", 'check_in_service')
    online_boarding = rating("Online Boarding", 'online_boarding')
    gate_location = rating("Gate Location", 'gate_location')
    on_board_service = rating("On-board Service", 'on_board_service')

with col4:
    seat_comfort = rating("Seat Comfort", 'seat_comfort')
    leg_room_service = rating("Leg Room Service", 'leg_room_service')
    cleanliness = rating("Cleanliness", 'cleanliness')
    food_and_drink = rating("Food and Drink", 'food_and_drink')
    in_flight_service = rating("In-flight Service", 'in_flight_service')
    in_flight_wifi_service = rating("In-flight Wifi Service", 'in_flight_wifi_service')
    in_flight_entertainment = rating("In-flight Entertainment", 'in_flight_entertainment')
    baggage_handling = rating("Baggage Handling", 'baggage_handling')

# Function to load scaler and model
def load_scaler_model():
    with open(r'D:\Bach Thao\DBM302m\airline_ratings\scaler.pkl', 'rb') as file:
        scaler = pickle.load(file)
    with open(r'D:\Bach Thao\DBM302m\airline_ratings\model.pkl', 'rb') as f:
        model = pickle.load(f)
    return scaler, model

def preprocessing_data(data):
    df = pd.DataFrame([data])

    feature_order = [
        'Gender', 'Age', 'Customer Type', 'Type of Travel', 'Class', 'Flight Distance',
        'Departure Delay', 'Arrival Delay', 'Departure and Arrival Time Convenience',
        'Ease of Online Booking', 'Check-in Service', 'Online Boarding', 'Gate Location',
        'On-board Service', 'Seat Comfort', 'Leg Room Service', 'Cleanliness', 'Food and Drink',
        'In-flight Service', 'In-flight Wifi Service', 'In-flight Entertainment', 'Baggage Handling'
    ]
    
    gender_mapping = {'Female': 0, 'Male': 1}
    customer_type_mapping = {'First-time': 0, 'Returning': 1}
    type_of_travel_mapping = {'Business': 0, 'Personal': 1}
    class_mapping = {'Business': 0, 'Economy': 1, 'Economy Plus': 2}

    df['Gender'] = df['Gender'].map(gender_mapping)
    df['Customer Type'] = df['Customer Type'].map(customer_type_mapping)
    df['Type of Travel'] = df['Type of Travel'].map(type_of_travel_mapping)
    df['Class'] = df['Class'].map(class_mapping)
    
    df = df.reindex(columns=feature_order)
    
    scaler, model = load_scaler_model()
    df_scaled = scaler.transform(df)
    
    return df_scaled, model

# Submit button
if st.button("Submit"):
    # Collect feedback
    feedback = {
        "Age": age,
        "Gender": gender,
        "Customer Type": customer_type,
        "Type of Travel": type_of_travel,
        "Class": travel_class,
        "Flight Distance": flight_distance,
        "Departure Delay": departure_delay,
        "Arrival Delay": arrival_delay,
        "Departure and Arrival Time Convenience": departure_arrival_time_convenience,
        "Ease of Online Booking": ease_of_online_booking,
        "Check-in Service": check_in_service,
        "Online Boarding": online_boarding,
        "Gate Location": gate_location,
        "On-board Service": on_board_service,
        "Seat Comfort": seat_comfort,
        "Leg Room Service": leg_room_service,
        "Cleanliness": cleanliness,
        "Food and Drink": food_and_drink,
        "In-flight Service": in_flight_service,
        "In-flight Wifi Service": in_flight_wifi_service,
        "In-flight Entertainment": in_flight_entertainment,
        "Baggage Handling": baggage_handling
    }
    
    st.write(feedback)
    
    df_scaled, model = preprocessing_data(feedback)
    result = model.predict(df_scaled)
    
    st.subheader('Result:')
    if result[0] == 0:
        st.write('Dissatisfaction')
    else:
        st.write('Satisfaction')
