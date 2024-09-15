# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# import os

# def send_email(directory, recipient_email):
#     """
#     Envía un correo electrónico con el resumen de las comisiones adjunto.

#     Args:
#         directory (str): El directorio donde se encuentra el archivo Excel.
#         recipient_email (str): Dirección de correo electrónico del destinatario.
#     """
#     sender_email = "correo@hotmail.com"  # Cambia esto por tu dirección de correo electrónico
#     subject = "Resumen de Comisiones"
#     body = "Adjunto encontrará el resumen de las comisiones para los meses correspondientes a julio y agosto de 2024."

#     # Crear el mensaje del correo
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = recipient_email
#     msg['Subject'] = subject
#     msg.attach(MIMEText(body, 'plain'))

#     # Encontrar el archivo Excel más reciente en el directorio
#     files = os.listdir(directory)
#     excel_files = [f for f in files if f.endswith('.xlsx')]
#     latest_file = max(excel_files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
#     file_path = os.path.join(directory, latest_file)

#     # Adjuntar el archivo Excel
#     with open(file_path, 'rb') as file:
#         part = MIMEApplication(file.read(), Name=latest_file)
#         part['Content-Disposition'] = f'attachment; filename="{latest_file}"'
#         msg.attach(part)

#     # Enviar el correo
#     with smtplib.SMTP('smtp.office365.com', 587) as server:
#         server.starttls()
#         server.login(sender_email, 'contraseña')  # Cambia esto por tu contraseña
#         server.send_message(msg)

#     print(f"Correo enviado a {recipient_email} con el archivo {latest_file}")

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os
from constants import email_credentials, smtp_settings  # Importa las configuraciones

def send_email(directory, recipient_email):
    """
    Envía un correo electrónico con el resumen de las comisiones adjunto.

    Args:
        directory (str): El directorio donde se encuentra el archivo Excel.
        recipient_email (str): Dirección de correo electrónico del destinatario.
    """
    sender_email = email_credentials['sender_email']
    sender_password = email_credentials['sender_password']
    smtp_server = smtp_settings['smtp_server']
    smtp_port = smtp_settings['smtp_port']
    
    subject = "Resumen de Comisiones"
    body = "Adjunto encontrará el resumen de las comisiones para los meses correspondientes a julio y agosto de 2024."

    # Crear el mensaje del correo
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Encontrar el archivo Excel más reciente en el directorio
    files = os.listdir(directory)
    excel_files = [f for f in files if f.endswith('.xlsx')]
    latest_file = max(excel_files, key=lambda f: os.path.getmtime(os.path.join(directory, f)))
    file_path = os.path.join(directory, latest_file)

    # Adjuntar el archivo Excel
    with open(file_path, 'rb') as file:
        part = MIMEApplication(file.read(), Name=latest_file)
        part['Content-Disposition'] = f'attachment; filename="{latest_file}"'
        msg.attach(part)

    # Enviar el correo
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

    print(f"Correo enviado a {recipient_email} con el archivo {latest_file}")

