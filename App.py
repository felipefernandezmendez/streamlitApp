import streamlit as st
from PIL import Image
import requests
import numpy as np
import time
from streamlit_extras.switch_page_button import switch_page
from streamlit_lottie import st_lottie

# Página principal
def main_page():
    st.title("The Most Random App Ever")
    st.write('<h4 style="font-size: 24px;">El hecho que hayas llegado asta aquí es un milagro </h4>', unsafe_allow_html=True)
    if st.button("Para Magia Click Aquí"):
        switch_page("Bien")

    st.write("---")

   
# Sistema de navegación
def main():
    main_page()

if __name__ == "__main__":
    main()
