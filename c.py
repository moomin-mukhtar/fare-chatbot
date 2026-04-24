import streamlit as st
from datetime import date

# -----------------------------
# 🇮🇳 Indian States
# -----------------------------
india_states = [
    "Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
    "Goa","Gujarat","Haryana","Himachal Pradesh","Jharkhand",
    "Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur",
    "Meghalaya","Mizoram","Nagaland","Odisha","Punjab",
    "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura",
    "Uttar Pradesh","Uttarakhand","West Bengal"
]

# -----------------------------
# 🌍 Countries (large list)
# -----------------------------
countries = [
"India","USA","UK","Canada","Australia","Germany","France",
"Japan","China","UAE","Singapore","Malaysia","Russia","Brazil",
"South Africa","Italy","Spain","Netherlands","Sweden","Norway",
"Finland","Denmark","Poland","Mexico","Indonesia","Thailand"
]

# -----------------------------
# 📏 Distance Logic
# -----------------------------
def get_distance(source, destination):
    if source == destination:
        return 0

    # Domestic travel
    if source in india_states and destination in india_states:
        return 300 + abs(hash(source) - hash(destination)) % 2000

    # International travel
    return 2000 + abs(hash(source) - hash(destination)) % 8000


# -----------------------------
# 💰 Fare Calculation
# -----------------------------
def calculate_fare(mode, distance, travel_date):
    pricing = {
        "Airplane": 6,
        "Train": 2,
        "Bus": 1,
        "Ship": 3
    }

    fare = distance * pricing[mode]

    # 📅 Weekend price increase
    if travel_date.weekday() in [5, 6]:  # Saturday/Sunday
        fare *= 1.2

    return round(fare, 2)


# -----------------------------
# ⏱ Travel Time
# -----------------------------
def travel_time(mode, distance):
    speed = {
        "Airplane": 600,
        "Train": 80,
        "Bus": 50,
        "Ship": 30
    }
    return round(distance / speed[mode], 2)


# -----------------------------
# 🎯 UI
# -----------------------------
st.title("🌍 Smart Transport Fare Chatbot")

# Travel type
mode_type = st.radio("Choose Travel Type", ["Domestic (India)", "International"])

# -----------------------------
# 📅 Date Inputs
# -----------------------------
travel_date = st.date_input("Select Travel Date", min_value=date.today())
return_date = st.date_input("Return Date (Optional)", min_value=travel_date)

# -----------------------------
# 🇮🇳 Domestic
# -----------------------------
if mode_type == "Domestic (India)":
    source = st.selectbox("Source State", india_states)
    destination = st.selectbox("Destination State", india_states)
    transport = st.selectbox("Transport Mode", ["Train", "Bus", "Airplane"])

# -----------------------------
# 🌍 International
# -----------------------------
else:
    source = st.selectbox("Source Country", countries)
    destination = st.selectbox("Destination Country", countries)
    transport = st.selectbox("Transport Mode", ["Airplane"])


# -----------------------------
# 🚀 Calculate
# -----------------------------
if st.button("Calculate Fare"):

    if source == destination:
        st.warning("Source and destination cannot be same")
    else:
        distance = get_distance(source, destination)
        fare = calculate_fare(transport, distance, travel_date)
        time = travel_time(transport, distance)

        st.success("✅ Travel Details")

        st.write(f"📍 From: {source}")
        st.write(f"📍 To: {destination}")
        st.write(f"📅 Travel Date: {travel_date}")
        st.write(f"🔁 Return Date: {return_date}")
        st.write(f"🛣 Distance: {distance} km")
        st.write(f"🚗 Mode: {transport}")
        st.write(f"💰 Fare: ₹{fare}")
        st.write(f"⏱ Travel Time: {time} hours")