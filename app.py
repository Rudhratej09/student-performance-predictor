import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("C:\\Users\\rudhr\\OneDrive\\Desktop\\code\\python aiml\\models\\student_model.pkl")

st.title(" Student Performance Predictor")

# User input
gender = st.selectbox("Gender", ['Male', 'Female'])
part_time_job = st.selectbox("Part-Time Job", ['Yes', 'No'])
diet_quality = st.selectbox("Diet Quality", ['Poor', 'Average', 'Good'])
parent_edu = st.selectbox("Parental Education Level", ['High School', 'College', 'Graduate'])
internet_quality = st.selectbox("Internet Quality", ['Poor', 'Average', 'Good'])
extracurricular = st.selectbox("Extracurricular Participation", ['Yes', 'No'])
exercise_freq = st.slider("Exercise Frequency (days/week)", 0, 7, 3)
netflix_hours = st.slider("Netflix Hours per Day", 0, 10, 2)
attendance = st.slider("Attendance (%)", 0, 100, 85)
social_media = st.slider("Social Media Hours", 0, 10, 3)
mental_health = st.slider("Mental Health Rating (1-10)", 1, 10, 7)
# Numeric inputs
study_hours = st.slider("Study Hours per Day", 0, 12, 3)
sleep_hours = st.slider("Sleep Hours per Day", 0, 12, 6)
screen_time = st.slider("Screen Time per Day", 0, 12, 4)

# Create dataframe
input_df = pd.DataFrame({
    'gender': [gender],
    'part_time_job': [part_time_job],
    'diet_quality': [diet_quality],
    'parental_education_level': [parent_edu],
    'internet_quality': [internet_quality],
    'extracurricular_participation': [extracurricular],
    'exercise_frequency': [exercise_freq],
    'study_hours_per_day': [study_hours],
    'netflix_hours': [netflix_hours],
    'attendance_percentage': [attendance],
    'social_media_hours': [social_media],
    'mental_health_rating': [mental_health],
    'sleep_hours': [sleep_hours]
})

# Predict
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Predicted Performance: {prediction:.2f} CGPA")