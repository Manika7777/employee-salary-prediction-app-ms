# app.py
import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("best_model.pkl")

# App settings
st.set_page_config(page_title="Salary Prediction", page_icon="💼", layout="centered")
st.title("💼 Employee Salary Prediction")
st.markdown("Predict whether an employee earns >50K or ≤50K based on key features.")

# User input (stacked vertically)
age = st.slider("Age", 18, 75, 30)
education = st.selectbox("Education", [
    "Bachelors", "Masters", "HS-grad", "Some-college", "Assoc-acdm", "Assoc-voc", 
    "Doctorate", "11th", "10th", "7th-8th", "Prof-school", "9th", "12th", 
    "5th-6th", "1st-4th", "Preschool"
])
occupation = st.selectbox("Occupation", [
    "Tech-support", "Craft-repair", "Other-service", "Sales", "Exec-managerial", 
    "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct", "Adm-clerical", 
    "Farming-fishing", "Transport-moving", "Priv-house-serv", "Protective-serv", 
    "Armed-Forces"
])
hours_per_week = st.slider("Hours per Week", 1, 80, 40)
experience = st.slider("Years of Experience", 0, 50, 5)

# Create input DataFrame
input_df = pd.DataFrame({
    'age': [age],
    'education': [education],
    'occupation': [occupation],
    'hours-per-week': [hours_per_week],
    'experience': [experience]
})

# Display user input
st.markdown("### 🔍 Input Summary")
st.dataframe(input_df)

# Predict on button click
if st.button("Predict Salary Class"):
    prediction = model.predict(input_df)
    result = ">50K" if prediction[0] == ">50K" or prediction[0] == 1 else "<=50K"
    st.success(f"✅ Prediction: Employee earns **{result}**")
