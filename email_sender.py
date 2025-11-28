import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "mail"
APP_PASSWORD= "pass mail app"
RECEIVER ="mail id"
msg = EmailMessage()
msg["From"] = EMAIL
msg["To"] = RECEIVER
msg["Subject"] = "HELLO..."
msg.set_content("this email was shared by python code...")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(EMAIL,APP_PASSWORD)
    server.send_message(msg)