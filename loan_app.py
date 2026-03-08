
import streamlit as st
import joblib
import numpy as np

model = joblib.load("loan_data_model.pkl")
prof_means = joblib.load("prof_means.pkl")
state_means = joblib.load("state_means.pkl")

st.title("Loan default prediction")

age = st.number_input("Age")
experiance = st.number_input("Experience")
current_job_years = st.number_input("Years in current job")
profession_label = st.selectbox(
    "Select your profession",
    options=list(prof_means.index),  # profession names
    index=None,
    placeholder="Type to search..."
)

if profession_label:
    profession_encoded = prof_means[profession_label]

state_label = st.selectbox(
    "Select your state",
    options=list(state_means.index),  # state names
    index=None,
    placeholder="Type to search..."
)
if state_label:
    state_encoded = state_means[state_label]


Car_Ownership = st.selectbox("Car ownership", ["yes","no"])
marriedSingle = st.selectbox("Married/Single", ["married","single"])
house_rented = st.selectbox("House rented", ["yes","no"])

if st.button("Predict Loan Default"):

    features = np.array([[age,experiance,current_job_years,profession_label,state_label,
                          1 if marriedSingle=="married" else 0,
                          1 if Car_Ownership=="yes" else 0,
                          1 if house_rented=="yes" else 0,
                          ]])

    prediction = model.predict(features)

    st.success(f"Estimated Loan default: {prediction[0]}")
    
