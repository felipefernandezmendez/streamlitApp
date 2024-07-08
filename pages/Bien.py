import streamlit as st
from PIL import Image
import requests
import numpy as np

def magia():
    st.title("Página Magia")
    st.write("Por favor, complete los siguientes campos:")

    # Campo para el número favorito
    numero_favorito = st.number_input("Número favorito", min_value=0, max_value=9, step=1, format="%d")

    # Campo para el signo del zodíaco
    signo_zodiaco = st.text_input("Signo del Zodíaco")

    # Campo para el animal preferido
    animal_preferido = st.selectbox("Animal preferido", ["Perro", "Gato"])

    # Mostrar los valores ingresados
    st.write(f"Tu número favorito es: {numero_favorito}")
    st.write(f"Tu signo del zodíaco es: {signo_zodiaco}")
    st.write(f"Tu animal preferido es: {animal_preferido}")

   # Botón para mostrar la imagen
    if st.button("Ahora. Aquí. La magia"):
        # Lista de imágenes
        imagenes = ["images/imagen1.jpg", "images/imagen2.jpg", "images/imagen3.jpg"]
        # Seleccionar una imagen aleatoria
        imagen_aleatoria = random.choice(imagenes)
        # Mostrar la imagen seleccionada
        st.image(imagen_aleatoria, use_column_width=True)
        
if __name__ == "__main__":
    magia()
    
    st.write("---")
