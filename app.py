import streamlit as st
from io import BytesIO
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# ---- Configuración de la página ----
st.set_page_config(page_title="Generador de QR para Encuestas", layout="centered")

st.title("📋 Generador de QR para Encuestas")

# ---- Inputs del usuario ----
nombre_actividad = st.text_input("📝 Ingresá el *nombre de la actividad*", placeholder="Ej: Word Básico")
codigo_curso = st.text_input("📌 Ingresá el *código del curso*", placeholder="Ej: word02")

# ---- Si ambos campos fueron completados ----
if nombre_actividad and codigo_curso:
    nombre_actividad = nombre_actividad.strip().upper()
    codigo_curso = codigo_curso.strip().upper()

    url = f"https://encuestas-dcycp.streamlit.app/?curso={codigo_curso}"
    st.markdown(f"🔗 URL generada: [{url}]({url})")

    # ---- Generar QR redondeado ----
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer()
    )

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    qr_bytes = buffer.getvalue()

    st.image(qr_bytes, caption="🖨️ Código QR estilo redondeado", use_container_width=False)

    # ---- Descargar QR ----
    nombre_archivo = f"QR-{nombre_actividad.replace(' ', '_')}.png"
    st.download_button(
        label="📥 Descargar QR",
        data=qr_bytes,
        file_name=nombre_archivo,
        mime="image/png"
    )


