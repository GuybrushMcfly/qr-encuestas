import streamlit as st
import qrcode
from io import BytesIO

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

    # ---- Generar QR ----
    qr = qrcode.make(url)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_bytes = buffer.getvalue()

    st.image(qr_bytes, caption="🖨️ Código QR generado", use_container_width=False)

    # ---- Descargar QR ----
    nombre_archivo = f"QR-{nombre_actividad.replace(' ', '_')}.png"
    st.download_button(
        label="📥 Descargar QR",
        data=qr_bytes,
        file_name=nombre_archivo,
        mime="image/png"
    )

