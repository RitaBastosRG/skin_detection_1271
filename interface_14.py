import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title = 'Skin Cancer Prediction',
    page_icon = '😇')

st.markdown(""" <style> .font {
font-size:64px; font-weight: 400; font-family: 'Newsreader'; font-style: normal; color: #000000;}
</style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Skin Cancer Prediction</p>', unsafe_allow_html=True)
st.markdown("""Check the health of your skin using our website and have the prediction.""")

def load_image():
    uploaded_file = st.file_uploader(label='Pick an image to test')
    if uploaded_file is not None:
        image_data = uploaded_file.getvalue()
        st.image(image_data)

def main():
    st.header('Image upload demo')
    load_image()


if __name__ == '__main__':
    main()
