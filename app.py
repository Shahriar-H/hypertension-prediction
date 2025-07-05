import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load('hypertension_model.pkl')

# Define the exact feature order used during model training
feature_order = ['age', 'gender', 'pulse_rate', 'systolic_bp', 'diastolic_bp',
                 'glucose', 'height', 'weight', 'bmi', 'family_diabetes',
                 'family_hypertension', 'cardiovascular_disease', 'stroke', 'diabetic']

st.title("Hypertension Risk Prediction App")

st.write("""
#### Enter patient data below:
""")

# Collect user input
height = st.number_input("Height (in meters)", min_value=1.0, max_value=2.5, value=1.70)
weight = st.number_input("Weight (in kg)", min_value=30, max_value=200, value=70)
age = st.number_input("Age", min_value=10, max_value=100, value=30)
gender = st.selectbox("Gender", ['Male', 'Female'])
systolic_bp = st.number_input("Systolic BP", min_value=80, max_value=200, value=120)
diastolic_bp = st.number_input("Diastolic BP", min_value=50, max_value=130, value=80)
glucose = st.number_input("Glucose Level", min_value=50, max_value=300, value=100)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=22.0)
pulse_rate = st.number_input("Pulse Rate", min_value=40, max_value=150, value=70)
diabetic = st.selectbox("Are you diabetic?", ['No', 'Yes'])
family_diabetes = st.selectbox("Family history of diabetes?", ['No', 'Yes'])
family_hypertension = st.selectbox("Family history of hypertension?", ['No', 'Yes'])
cardiovascular_disease = st.selectbox("Cardiovascular disease?", ['No', 'Yes'])
stroke = st.selectbox("History of stroke?", ['No', 'Yes'])

# Map inputs
gender = 1 if gender == 'Female' else 0
diabetic = 1 if diabetic == 'Yes' else 0
family_diabetes = 1 if family_diabetes == 'Yes' else 0
family_hypertension = 1 if family_hypertension == 'Yes' else 0
cardiovascular_disease = 1 if cardiovascular_disease == 'Yes' else 0
stroke = 1 if stroke == 'Yes' else 0

# Create input DataFrame with all features
input_data = pd.DataFrame({
    'age': [age],
    'gender': [gender],
    'pulse_rate': [pulse_rate],
    'systolic_bp': [systolic_bp],
    'diastolic_bp': [diastolic_bp],
    'glucose': [glucose],
    'height': [height],
    'weight': [weight],
    'bmi': [bmi],
    'family_diabetes': [family_diabetes],
    'family_hypertension': [family_hypertension],
    'cardiovascular_disease': [cardiovascular_disease],
    'stroke': [stroke],
    'diabetic': [diabetic]
})

# Reorder columns to match the model's expected input
input_data = input_data[feature_order]

# Predict
if st.button("Predict Hypertension"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ High Risk of Hypertension")
    else:
        st.success("✅ Low Risk of Hypertension")
