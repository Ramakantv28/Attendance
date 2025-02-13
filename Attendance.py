import streamlit as st
from geopy.distance import geodesic

# Define the allowed geographical area (latitude, longitude)
allowed_area = (28.5810, 77.0571)  # Example coordinates for Bangalore

# Function to check if the user is within the allowed area
def is_within_allowed_area(user_location):
    distance = geodesic(user_location, allowed_area).km
    return distance <= 1  # Allow within 1 km radius

# Streamlit app
st.title("Employee Attendance")

# Simulate user authentication (for demonstration purposes)
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    # Simulate location retrieval (for demonstration purposes)
    user_location = (12.9716, 77.5946)  # Example user location

    if is_within_allowed_area(user_location):
        st.success("You are within the allowed area. Attendance marked!")
    else:
        st.error("You are outside the allowed area. Attendance not marked.")
