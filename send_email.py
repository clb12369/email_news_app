import smtplib, ssl
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Access secrets
app_username = os.environ.get("USERNAME")
app_password = os.environ.get("APP_PASSWORD")
email_receiver = os.environ.get("RECEIVER")

def send_email(message):
    host = "smtp.google.com"
    port = 465

    username = app_username
    password = app_password

    receiver = email_receiver
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)