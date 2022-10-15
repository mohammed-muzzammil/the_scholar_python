# Aim is to develop a Text to Image WEB APP using Streamlit with the help of deep ai apis

# Importing the required libraries
import streamlit as st
import requests


# Function to fire the api
def generate_image(text):
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': text,
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    )
    # Return the image
    return r.json()['output_url']


# Title of the Web App
st.title("Text to Image Generator")

# Text Input
text = st.text_input("Enter the text")
button = st.button("Generate")
if button:
    st.write("Generating Image...")
    image = generate_image(text)
    st.image(image)
