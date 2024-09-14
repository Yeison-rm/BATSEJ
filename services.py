import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(commissions_df):
    """
    Envía un correo electrónico con el resumen de las comisiones adjunto.

    Args:
        commissions_df (pd.DataFrame): DataFrame con el resumen de las comisiones.
    """
    sender_email = "ramirezyeison115@hotmail.com"
    receiver_email = "receiver_email@example.com"
    subject = "Resumen de Comisiones"
    body = "Adjunto encontrará el resumen de las comisiones para los meses de julio y agosto de 2024."

    # Configurar el mensaje del correo
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo Excel
    with open('results/commissions_summary.xlsx', 'rb') as file:
        part = MIMEApplication(file.read(), Name='commissions_summary.xlsx')
        part['Content-Disposition'] = 'attachment; filename="commissions_summary.xlsx"'
        msg.attach(part)

    # Enviar el correo
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, 'your_password')
        server.send_message(msg)