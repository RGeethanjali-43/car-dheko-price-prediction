import streamlit as st

st.title("Used Car Price Prediction")

# Dropdowns for user input
model = st.sidebar.selectbox("Select Car Model:", ["Model A", "Model B", "Model C"])  # Example models
year = st.sidebar.selectbox("Select Model Year:", range(2000, 2024))
owner_no = st.sidebar.selectbox("Number of Previous Owners:", [1, 2, 3, 4])
mileage = st.sidebar.slider("Enter Mileage (in km):", 0, 200000, 50000)
engine = st.sidebar.selectbox("Select Engine Type:", ["Petrol", "Diesel", "Hybrid", "Electric"])
transmission = st.sidebar.selectbox("Select Transmission Type:", ["Manual", "Automatic"])
seats = st.sidebar.selectbox("Number of Seats:", [2, 4, 5, 7])
color = st.sidebar.selectbox("Select Color:", ["White", "Black", "Silver", "Red", "Blue"])

# Display the selected inputs
st.write(f"Selected Model: {model}")
st.write(f"Model Year: {year}")
st.write(f"Previous Owners: {owner_no}")
st.write(f"Mileage: {mileage} km")
st.write(f"Engine Type: {engine}")
st.write(f"Transmission: {transmission}")
st.write(f"Number of Seats: {seats}")
st.write(f"Color: {color}")

# Add further logic for prediction or data processing here
