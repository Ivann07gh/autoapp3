import streamlit as st
import pyshorteners
import qrcode
import os

# ESCORÇADOR D'URLs

def shorten_url(url):
    acort = pyshorteners.Shortener()
    url_acortada = acort.tinyurl.short(url)
    return url_acortada


st.set_page_config(
    page_title="Escurçador d'URLs i Generador de QRs",
    layout="centered"
)

st.header("ESCURÇADOR D'URLs")

st.text("""
Introduiu l'URL dins el requadre proporcionat. Posteriorment, presioneu el botó
"Genera una URL Escurçada" i automàticament serà retornada l'URL escurçada.
""")

url = st.text_input("Introdueix la URL")
if st.button("Genera una URL Escurçada"):
    st.write(
        "URL Escurçada amb èxit: ",
        shorten_url(url)
)

# GENERADOR DE CODIS QR

output_qr = "documents/qr_generat.png"

def generate_qr_code(url, output_qr):
    qr = qrcode.QRCode(
        version=7,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(
    fill_color="black",
    back_color="white"
    )
    img.save(output_qr)

st.header("GENERADOR DE CODIS QR")

st.text("""
Introduiu l'URL dins el requadre proporcionat. Posteriorment, presioneu el botó
"Genera el teu Codi QR" i de forma automàtica serà retornat un codi QR enllaçat
a la URL proporcionada.
""")

url = st.text_input("Introdueix la teva URL")

if st.button("Genera el teu Codi QR"):
    generate_qr_code(url, output_qr)
    st.image(
        output_qr,
        use_column_width=True
        )
    with open(output_qr, "rb") as f:
        image_data = f.read()  
    download = st.download_button(label="Descarrega el codi QR", data=image_data, file_name="qr_generat_png")
    os.remove("documents/qr_generat.png")