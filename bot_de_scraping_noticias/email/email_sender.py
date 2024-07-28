from flask_mail import Mail, Message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, body, recipients):
    mail = Mail()
    msg = MIMEMultipart()
    msg['From'] = 'your_email@example.com'
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    mail.send(msg)
