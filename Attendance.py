# import streamlit as st
# from geopy.distance import geodesic

# # Define the allowed geographical area (latitude, longitude)
# allowed_area = (28.5810, 77.0571)  # Example coordinates for Bangalore

# # Function to check if the user is within the allowed area
# def is_within_allowed_area(user_location):
#     distance = geodesic(user_location, allowed_area).km
#     return distance <= 10  # Allow within 1 km radius

# # Streamlit app
# st.title("Employee Attendance")

# # Simulate user authentication (for demonstration purposes)
# username = st.text_input("Username")
# password = st.text_input("Password", type="password")

# if st.button("Login"):
#     # Simulate location retrieval (for demonstration purposes)
#     user_location = (12.9716, 77.5946)  # Example user location

#     if is_within_allowed_area(user_location):
#         st.success("You are within the allowed area. Attendance marked!")
#     else:
#         st.error("You are outside the allowed area. Attendance not marked.")

import streamlit as st
from geopy.distance import geodesic
import requests

# Define the allowed geographical area (latitude, longitude) for Dwarka Sector 10 metro station
allowed_area = (28.5811, 77.0575)

# Function to check if the user is within the allowed area
def is_within_allowed_area(user_location):
    distance = geodesic(user_location, allowed_area).km
    return distance <= 1  # Allow within 1 km radius

# Function to get user's location based on IP address
def get_user_location():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        loc = data['loc'].split(',')
        return float(loc[0]), float(loc[1])
    except Exception as e:
        st.error(f"Error retrieving location: {e}")
        return None

# Streamlit app
st.title("Employee Attendance")

# Simulate user authentication (for demonstration purposes)
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    user_location = get_user_location()
    
    if user_location and is_within_allowed_area(user_location):
        st.success("You are within the allowed area. Attendance marked!")
    else:
        st.error("You are outside the allowed area. Attendance not marked.")
