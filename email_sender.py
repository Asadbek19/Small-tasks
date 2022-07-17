import os
import smtplib
from email.message import EmailMessage

EMAIL = 'Sender email'
EMAIL_PASSWORD = 'Email password'
PORT = 'Here must be PORT'
SERVER = 'Here must be server'


class SendGmail:
    def __init__(self, sender_email, email_password):
        self.sender = sender_email
        self.password = email_password
        self.port = PORT
        self.server = SERVER

    def send_message(self, receiver: str, subject: str, message: str) -> None:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = receiver
        msg.set_content(message)

        with smtplib.SMTP_SSL(self.server, int(self.port)) as smtp:
            aa = smtp.login(self.sender, self.password)
            print(aa)
            smtp.send_message(msg)


Email = SendGmail(    
    sender_email=EMAIL,
    email_password=EMAIL_PASSWORD
)


Email.send_message(
    receiver="Here must be receiver",
    subject='Here must be subject of message',
    message='ATTENTION! This message sended automatically from Python code.'
)

# This is a simple auto-send script via python code.