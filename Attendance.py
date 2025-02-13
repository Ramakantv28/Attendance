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
    function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(showPosition, showError);
        } else {
            document.getElementById("location").value = "Geolocation is not supported by this browser.";
            document.getElementById("location-form").submit();
        }
    }

    function showPosition(position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        const location = `${latitude},${longitude}`;
        document.getElementById("location").value = location;
        document.getElementById("location-form").submit();
    }

    function showError(error) {
        switch(error.code) {
            case error.PERMISSION_DENIED:
                alert("User denied the request for Geolocation.");
                break;
            case error.POSITION_UNAVAILABLE:
                alert("Location information is unavailable.");
                break;
            case error.TIMEOUT:
                alert("The request to get user location timed out.");
                break;
            case error.UNKNOWN_ERROR:
                alert("An unknown error occurred.");
                break;
        }
        document.getElementById("location").value = "Error retrieving location.";
        document.getElementById("location-form").submit();
    }

    getLocation();
    </script>
    <form id="location-form" action="" method="GET">
        <input type="hidden" name="location" id="location">
    </form>
    """
    st.components.v1.html(location_script)

    # Get user's location from query parameters
    user_location = st.query_params.get('location')
    
    if user_location and "Error" not in user_location[0]:
        user_location = tuple(map(float, user_location[0].split(',')))
        if is_within_allowed_area(user_location):
            st.success("You are within the allowed area. Attendance marked!")
        else:
            st.error("You are outside the allowed area. Attendance not marked.")
    else:
        st.error("Unable to retrieve location from browser. Please ensure location access is allowed.")
        
        # Manual input for location
        st.write("If the automatic location retrieval fails, please enter your coordinates manually below:")
        latitude = st.number_input("Latitude", format="%.6f")
        longitude = st.number_input("Longitude", format="%.6f")
        
        if st.button("Submit Location"):
            user_location = (latitude, longitude)
            if is_within_allowed_area(user_location):
                st.success("You are within the allowed area. Attendance marked!")
            else:
                st.error("You are outside the allowed area. Attendance not marked.")
