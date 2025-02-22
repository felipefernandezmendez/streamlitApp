import streamlit as st
from PIL import Image
import requests
import numpy as np
import random
import os

def magia():
    st.title("Has llegado a la Magia")
    st.write("Complete los siguientes campos hechizado:")

    # Campo para el número favorito
    numero_favorito = st.number_input("Número favorito", min_value=0, max_value=9, step=1, format="%d")

    # Campo para el signo del zodíaco
    signo_zodiaco = st.text_input("Signo del Zodíaco")

    # Campo para el animal preferido
    animal_preferido = st.selectbox("Animal preferido", ["Perro", "Gato"])


   # Botón para mostrar el texto
    if st.button("Ahora. Aquí. La magia"):
        # Lista de textos
        textos = ["ABRACADABRA XD", "ALACAZAM... MAGIA", "SIGUE PARTICIPANDO"]
        # Seleccionar un texto aleatorio
        texto_aleatorio = random.choice(textos)
        # Mostrar el texto seleccionado con estilo
        st.markdown(f"<h1 style='text-align: center; color: red;'>{texto_aleatorio}</h1>", unsafe_allow_html=True)
  
  # Lista de imágenes
        imagenes = ["__pycache__/images/descarga (1).jfif", "__pycache__/images/descarga (2).jfif", "__pycache__/images/images (1).jfif"]
        # Seleccionar una imagen aleatoria
        imagen_aleatoria = random.choice(imagenes)
        # Mostrar la imagen seleccionada
        st.image(imagen_aleatoria, use_column_width=True)

        
if __name__ == "__main__":
    magia()
    
    st.write("---")
