import streamlit as st
import pandas as pd

# Title
st.title("Hello World")

# Text input
name = st.text_input("Enter your name")

# Number input
age = st.number_input("Enter your age", min_value=0, max_value=100)

# Selectbox # The first option is the default
occupation = st.selectbox("What is your occupation", ["None", "Student", "Teacher", "Doctor"])

# Multi-Selectbox # The variable is a list of selected options
occupations = st.multiselect("What are your occupations", ["None", "Student", "Teacher", "Doctor"])

# Checkbox # The variable is a boolean True or False
ocu = st.checkbox("Are you a student?")

# Radio # The first option is the default
ocu_radio = st.radio("What is your occupation", ["None", "Student", "Teacher", "Doctor"])

# Slider # Slider is used for continuous values (Numerical)
age_slider = st.slider("How old are you?", min_value=50, max_value=100, step=5)

# Button # Used to trigger an action
button = st.button("Click me")
if button:
    st.write("You clicked the button")

# Date input
date = st.date_input("When is your birthday?")

# File Upload for csv and xlsx files
file = st.file_uploader("Upload your file", type=["csv", "xlsx"])
if file and file.name.endswith("csv"):
    df = pd.read_csv(file)
    st.write(df)
elif file and file.name.endswith("xlsx"):
    df = pd.read_excel(file)


# Output the data
st.write("Output")
st.write(123)





