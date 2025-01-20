import streamlit as st
import pandas as pd
from datetime import datetime

# Configuración inicial
st.set_page_config(page_title="Compra y Venta de Autos", page_icon="🚗", layout="wide")

# Base de datos simulada
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["Nombre", "Email", "Teléfono", "Tipo", "Marca", "Modelo", "Año", "Estado", "Papeles", "Descripción", "Fecha"])

# Encabezado
st.title("Compra y Venta de Autos")
st.markdown("Subí tu auto para vender o encontrá el auto que buscás.")

# Mostrar registros
def mostrar_registros():
    st.subheader("Autos publicados")
    if st.session_state["data"].empty:
        st.info("Aún no hay autos publicados.")
    else:
        st.dataframe(st.session_state["data"])

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

            # Botón de envío
            enviado = st.form_submit_button("Enviar")

            if enviado:
                nuevo_registro = {
                    "Nombre": nombre,
                    "Email": email,
                    "Teléfono": telefono,
                    "Tipo": tipo,
                    "Marca": marca,
                    "Modelo": modelo,
                    "Año": anio,
                    "Estado": estado,
                    "Papeles": papeles,
                    "Descripción": descripcion,
                    "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                st.session_state["data"] = st.session_state["data"].append(nuevo_registro, ignore_index=True)
                st.success("Datos enviados correctamente!")

# Botón flotante de WhatsApp
whatsapp_button = """
<style>
#whatsapp {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #25D366;
    color: white;
    border-radius: 50%;
    width: 60px;
    height: 60px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 30px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    z-index: 100;
    cursor: pointer;
}
#whatsapp a {
    color: white;
    text-decoration: none;
}
</style>
<div id="whatsapp">
    <a href="https://wa.me/+5492664502682?text=Vengo%20del%20site%20y%20quiero%20más%20info%20para%20comprar%20o%20vender%20mi%20auto" target="_blank">&#128172;</a>
</div>
"""

# Render de las secciones
mostrar_registros()
cargar_datos()
st.markdown(whatsapp_button, unsafe_allow_html=True)
