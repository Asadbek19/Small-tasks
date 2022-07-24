import smtplib
import os
from email.mime.text import MIMEText

def send_email(message, subject):
    sender = 'Here must be sender email'
    password = 'Here must be email password'

    receiver = "Here must be recipient's email address"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = subject
        server.sendmail(sender, receiver, msg.as_string())

        return "The message was sent succesfully!"

    except Exception as _ex:
        return f"{_ex}\Check your login or password please!"


def main():
    subject = input("Type your message subject: ")
    message = input("Type your message: ")
    print(send_email(subject=subject, message=message))

if __name__ == "__main__":
    main()

# This is a simple auto-send script via Python code
# with the ability to enter the subject and message
#    of the email via the console.