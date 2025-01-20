import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image

# Configuración inicial
st.set_page_config(page_title="Compra y Venta de Autos", page_icon="🚗", layout="wide")

# Base de datos simulada
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["Nombre", "Email", "Teléfono", "Tipo", "Marca", "Modelo", "Año", "Estado", "Papeles", "Descripción", "Fecha"])

# Encabezado
st.image("logof.png", width=400)
st.markdown("<h1 style='text-align: center;'>Compra y Venta de Autos</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Compra y Vende con Confianza</h3>", unsafe_allow_html=True)

# Mostrar autos publicados con slider
def mostrar_autos_publicados():
    st.subheader("Autos publicados")
    imagenes_publicadas = ["11.png", "12.png", "8.png", "9.png"]  # Lista de imágenes subidas por la empresa

    if not imagenes_publicadas:
        st.info("Aún no hay autos publicados.")
    else:
        st.image(imagenes_publicadas, caption=["Auto 1", "Auto 2", "Auto 3", "Auto 4"], width=400, use_column_width="auto")

# Ficha para cargar datos
def cargar_datos():
    with st.expander("Completar ficha para publicar un auto"):
        with st.form("formulario_auto"):
            st.subheader("Formulario para comprar o vender un auto")

            # Información del usuario
            nombre = st.text_input("Nombre", max_chars=50)
            email = st.text_input("Email", max_chars=50)
            telefono = st.text_input("Teléfono de contacto", max_chars=20)
            tipo = st.radio("Qué querés hacer?", ["Comprar", "Vender"])

            # Datos del vehículo
            marca = st.text_input("Marca del auto", max_chars=30)
            modelo = st.text_input("Modelo del auto", max_chars=30)
            anio = st.number_input("Año del auto", min_value=1900, max_value=datetime.now().year, step=1)
            estado = st.selectbox("Estado del auto", ["Nuevo", "Usado"])
            papeles = st.radio("Papeles al día?", ["Sí", "No"])
            descripcion = st.text_area("Descripción adicional")

            # Subida de imágenes
            imagenes = st.file_uploader("Subí hasta 3 imágenes del auto", type=["jpg", "jpeg", "png"], accept_multiple_files=True, key="imagenes_auto")

            #
