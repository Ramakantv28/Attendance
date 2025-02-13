import streamlit as st
from geopy.distance import geodesic

# Define the allowed geographical area (latitude, longitude) for Dwarka Sector 10 metro station
allowed_area = (28.5811, 77.0575)

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
    # JavaScript to get the user's location
    location_script = """
    <script>
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            const location = `${latitude},${longitude}`;
            document.getElementById("location").value = location;
            document.getElementById("location-form").submit();
        },
        (error) => {
            console.error(error);
        }
    );
    </script>
    <form id="location-form" action="" method="GET">
        <input type="hidden" name="location" id="location">
    </form>
    """
    st.components.v1.html(location_script)

    # Get user's location from query parameters
    user_location = st.query_params.get('location')
    
    if user_location:
        user_location = tuple(map(float, user_location[0].split(',')))
        if is_within_allowed_area(user_location):
            st.success("You are within the allowed area. Attendance marked!")
        else:
            st.error("You are outside the allowed area. Attendance not marked.")
    else:
        st.error("Unable to retrieve location from browser.")
