
import streamlit as st
import joblib
import numpy as np

model = joblib.load("loan_data_model.pkl")
prof_means = joblib.load("prof_means.pkl")
state_means = joblib.load("state_means.pkl")

st.title("Loan Default Prediction")

age = st.number_input("Age")
experiance = st.number_input("Experience")
current_job_years = st.number_input("Years in current job")

profession_encoded = None
state_encoded = None

profession_label = st.selectbox("Select your profession", options=list(prof_means.index), index=None, placeholder="Type to search...")
if profession_label:
    profession_encoded = prof_means[profession_label]

state_label = st.selectbox("Select your state", options=list(state_means.index), index=None, placeholder="Type to search...")
if state_label:
    state_encoded = state_means[state_label]

Car_Ownership = st.selectbox("Car ownership", ["yes","no"])
marriedSingle = st.selectbox("Married/Single", ["married","single"])
house_rented = st.selectbox("House rented", ["yes","no"])

if st.button("Predict Loan Default"):
    if profession_encoded is None or state_encoded is None:
        st.warning("Please select a profession and state first.")
    else:
        features = np.array([[
            age,
            experiance,
            1 if marriedSingle=="married" else 0,
            1 if house_rented=="yes" else 0,
            1 if Car_Ownership=="yes" else 0,
            state_encoded,
            profession_encoded,
            current_job_years
        ]])
        prediction = model.predict(features)
        st.success(f"Estimated Loan Default: {prediction[0]}")
