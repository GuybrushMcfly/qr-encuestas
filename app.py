import streamlit as st
import qrcode
from io import BytesIO

# ---- CONFIGURACIÓN DE LA PÁGINA ----
st.set_page_config(page_title="Generador de QR para Encuestas", layout="centered")

st.title("🎯 Generador de URL + Código QR para Encuestas")

# ---- ENTRADA DEL CÓDIGO DE CURSO ----
codigo = st.text_input("📌 Ingresá el código del curso (ej: word02):", max_chars=20)

# ---- GENERACIÓN DE URL Y QR ----
if codigo:
    url_final = f"https://encuestas-dcycp.streamlit.app/?curso={codigo}"
    st.markdown(f"🔗 URL generada: **[{url_final}]({url_final})**")

    # Generar QR
    qr = qrcode.make(url_final)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    qr_bytes = buffer.getvalue()

    # Mostrar QR
    st.image(qr_bytes, caption="Código QR", use_column_width=False)

    # Botón para descargar
    nombre_archivo = f"QR-{codigo}.png"
    st.download_button(
        label="⬇️ Descargar QR",
        data=qr_bytes,
        file_name=nombre_archivo,
        mime="image/png"
    )
else:
    st.info("Ingresá un código de curso para generar la URL y el QR.")
