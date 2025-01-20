import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image
from streamlit.components.v1 import html

# Configuración inicial
st.set_page_config(page_title="Compra y Venta de Autos", page_icon="🚗", layout="wide")

# Base de datos simulada
if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame(columns=["Nombre", "Email", "Teléfono", "Tipo", "Marca", "Modelo", "Año", "Estado", "Papeles", "Descripción", "Fecha"])

# Encabezado
st.image("logof.png", width=300)
st.markdown("<h1 style='text-align: center;'>Compra y Venta de Autos</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Compra y Vende con Confianza</h3>", unsafe_allow_html=True)

# Mostrar autos publicados con interactividad

def mostrar_autos_publicados():
    st.subheader("Autos publicados")
    imagenes_publicadas = ["11.png", "12.png", "8.png", "9.png"]  # Lista de imágenes subidas por la empresa

    if not imagenes_publicadas:
        st.info("Aún no hay autos publicados.")
    else:
        selected_image_index = st.selectbox("Seleccioná un auto para más información", options=range(len(imagenes_publicadas)), format_func=lambda i: f"Auto {i + 1}")
        st.image(imagenes_publicadas[selected_image_index], caption=f"Vista del auto {selected_image_index + 1}", use_column_width=True)

        if st.button("Completar ficha para este auto"):
            st.session_state.show_form = True

# Ficha para cargar datos

def cargar_datos():
    if "show_form" in st.session_state and st.session_state.show_form:
        st.subheader("Completar ficha para publicar un auto")
        with st.form("formulario_auto", clear_on_submit=True):
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

            # Botón de envío
            enviado = st.form_submit_button("Enviar")

            if enviado:
                if imagenes and len(imagenes) > 3:
                    st.error("Solo podés subir hasta 3 imágenes.")
                else:
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

                    # Mensaje de WhatsApp
                    mensaje = (
                        f"Hola, soy {nombre}.\n"
                        f"Tipo: {tipo}.\n"
                        f"Marca: {marca}, Modelo: {modelo}, Año: {anio}.\n"
                        f"Estado: {estado}, Papeles al día: {papeles}.\n"
                        f"Descripción: {descripcion}.\n"
                        f"Teléfono: {telefono}"
                    )
                    enlace_whatsapp = f"https://wa.me/+5492664502682?text={mensaje.replace(' ', '%20').replace('\n', '%0A')}"

                    st.success("Datos enviados correctamente!")
                    st.markdown(f"[Enviar datos por WhatsApp]({enlace_whatsapp})", unsafe_allow_html=True)
                st.session_state.show_form = False

# Botón flotante de WhatsApp y enlace a ficha
floating_buttons = """
<style>
#buttons {
    position: fixed;
    bottom: 80px;
    right: 20px;
    z-index: 100;
}
.button {
    margin-bottom: 10px;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    cursor: pointer;
    text-decoration: none;
    color: white;
}
#whatsapp {
    background-color: #25D366;
}
</style>
<div id="buttons">
    <a id="whatsapp" class="button" href="https://wa.me/+5492664502682?text=Vengo%20del%20site%20y%20quiero%20más%20info%20para%20comprar%20o%20vender%20mi%20auto" target="_blank">💬</a>
</div>
"""

# Footer
footer = """
<style>
#footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    background-color: #f1f1f1;
    text-align: center;
    padding: 10px 0;
    font-size: 14px;
    color: #333;
}
#footer a {
    color: #007BFF;
    text-decoration: none;
    font-weight: bold;
}
#footer a:hover {
    text-decoration: underline;
}
</style>
<div id="footer">
    Powered by <a href="https://instagram.com/vasco.soro" target="_blank">vasco.soro</a>
</div>
"""

# Render de las secciones
mostrar_autos_publicados()
cargar_datos()
st.markdown(floating_buttons, unsafe_allow_html=True)
st.markdown(footer, unsafe_allow_html=True)
