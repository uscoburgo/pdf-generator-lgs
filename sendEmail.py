import re
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


def enviaMail():
    """configurando correo"""
    key = os.getenv("repass")
    message = MIMEMultipart('alternative')
    message['Subject'] = 'Reporte de producción de alimentos'
    message['From'] = 'letsgosurfingapp@gmail.com'
    message['To'] = 'uscoburgo@gmail.com'
    receptor = input(str("Introduce el e-mail donde quieres enviar el reporte: "))


    # PARA ENVIAR EL ARCHIVO ADJUNTO
    nombre_adjunto = "Report"
    archivo_adjunto = open("forecastPDF.pdf", 'rb')
    # Creamos un objeto MIME base
    message.attach(MIMEText("Hi, please find attached the PDF report with the surf forecast. STAY RIDIN'!", 'plain'))
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    #Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', f"attachment; filename= {nombre_adjunto}.pdf",)
    # Y finalmente lo agregamos al mensaje
    message.attach(adjunto_MIME)
    text = message.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('letsgosurfingapp@gmail.com', f'{key}')
    server.sendmail('uscoburgo@gmail.com', f'{receptor}', text)
    server.quit()