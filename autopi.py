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

if "show_form" not in st.session_state:
    st.session_state["show_form"] = False

# Encabezado
st.image("logof.png", width=300)
st.markdown("<h1 style='text-align: center; text-transform: uppercase;'>Compra y Venta de Autos</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Compra y vende con transparencia, seguridad y respaldo</h3>", unsafe_allow_html=True)

# Mostrar autos publicados con diseño estilo revista
def mostrar_autos_publicados():
    st.subheader("Autos publicados")
    imagenes_publicadas = ["11.png", "12.png", "8.png", "9.png"]  # Lista de imágenes subidas por la empresa

    if not imagenes_publicadas:
        st.info("Aún no hay autos publicados.")
    else:
        cols = st.columns(2)  # Dividir en dos columnas para diseño estilo revista
        for index, img in enumerate(imagenes_publicadas):
            with cols[index % 2]:
                st.image(img, caption=f"Auto {index + 1}", use_container_width=True)
                enlace_whatsapp = f"https://wa.me/+5492664502682?text=Quiero%20info%20sobre%20este%20auto:%20{img}"
                st.markdown(f"[Quiero info sobre este auto]({enlace_whatsapp})", unsafe_allow_html=True)
                st.markdown("---")

# Ficha para cargar datos
def cargar_datos():
    with st.expander("¡Completá la ficha para publicar un auto!", expanded=st.session_state["show_form"]):
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
                        f"Hola, soy {nombre}.
"
                        f"Tipo: {tipo}.
"
                        f"Marca: {marca}, Modelo: {modelo}, Año: {anio}.
"
                        f"Estado: {estado}, Papeles al día: {papeles}.
"
                        f"Descripción: {descripcion}.
"
                        f"Teléfono: {telefono}"
                    )
                    enlace_whatsapp = f"https://wa.me/+5492664502682?text={mensaje.replace(' ', '%20').replace('\n', '%0A')}"

                    st.success("Datos enviados correctamente!")
                    st.markdown(f"[Enviar datos por WhatsApp]({enlace_whatsapp})", unsafe_allow_html=True)

# Nuevo botón flotante visible con logow.png
floating_buttons = """
<style>
#buttons {
    position: fixed;
    bottom: 80px;
    right: 20px;
    z-index: 100;
}
#whatsapp-button {
    width: 70px;
    height: 70px;
    background-image: url('logow.png');
    background-size: cover;
    background-repeat: no-repeat;
    border: 2px solid white;
    border-radius: 50%;
    cursor: pointer;
    display: block;
}
</style>
<div id="buttons">
    <a id="whatsapp-button" href="https://wa.me/+5492664502682?text=Vengo%20del%20site%20y%20quiero%20más%20info%20para%20comprar%20o%20vender%20mi%20auto" target="_blank"></a>
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
