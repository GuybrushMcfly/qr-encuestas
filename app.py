import streamlit as st
from io import BytesIO
import qrcode
from PIL import Image, ImageDraw, ImageFont
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# ---- Configuración de la página ----
st.set_page_config(page_title="QR con texto central", layout="centered")
st.title("📋 Generador de QR con texto en el centro")

# ---- Inputs ----
nombre_actividad = st.text_input("📝 Nombre de la actividad", placeholder="Ej: Word Básico")
codigo_curso = st.text_input("📌 Código del curso", placeholder="Ej: word02")

if nombre_actividad and codigo_curso:
    nombre_actividad = nombre_actividad.strip().upper()
    codigo_curso = codigo_curso.strip().upper()
    url = f"https://encuestas-dcycp.streamlit.app/?curso={codigo_curso}"
    st.markdown(f"🔗 URL generada: [{url}]({url})")

    # ---- Generar QR estilizado ----
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    qr.make(fit=True)
    img_qr = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=RoundedModuleDrawer()
    ).convert("RGBA")

    # ---- Dibujar el nombre en el centro ----
    draw = ImageDraw.Draw(img_qr)
    ancho, alto = img_qr.size

    # Fuente y tamaño dinámico
    try:
        fuente = ImageFont.truetype("arial.ttf", size=20)
    except:
        fuente = ImageFont.load_default()

    texto = nombre_actividad
    text_width, text_height = draw.textsize(texto, font=fuente)

    # Fondo blanco detrás del texto (como una etiqueta)
    padding = 10
    box = [
        (ancho - text_width) // 2 - padding,
        (alto - text_height) // 2 - padding,
        (ancho + text_width) // 2 + padding,
        (alto + text_height) // 2 + padding
    ]
    draw.rectangle(box, fill="white", outline=None)
    draw.text(
        ((ancho - text_width) // 2, (alto - text_height) // 2),
        texto,
        font=fuente,
        fill="black"
    )

    # ---- Mostrar y descargar ----
    buffer = BytesIO()
    img_qr.save(buffer, format="PNG")
    qr_bytes = buffer.getvalue()

    st.image(qr_bytes, caption="🖨️ QR con texto en el centro", use_container_width=False)

    nombre_archivo = f"QR-{nombre_actividad.replace(' ', '_')}.png"
    st.download_button("📥 Descargar QR", data=qr_bytes, file_name=nombre_archivo, mime="image/png")



