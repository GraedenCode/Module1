import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")

with st.expander('Start Camera'):
    # start camera
    camera_image = st.camera_input('')


if camera_image:
    # create a pillow image instance
    img = Image.open(camera_image)

    # convert the pillow image to gray scale
    gray_img = img.convert('L')

    # Render the gray scale image on the webpage
    st.image(gray_img)

if uploaded_image:
    # create a pillow image instance
    img = Image.open(uploaded_image)

    # convert the pillow image to gray scale
    gray_img = img.convert('L')

    # Render the gray scale image on the webpage
    st.image(gray_img)