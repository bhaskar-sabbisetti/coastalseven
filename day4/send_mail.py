import smtplib
from email.message import EmailMessage


SENDER_EMAIL = "bhaskarsabbisetti@gmail.com"
APP_PASSWORD = "dxec fojq satb zsfv"   
RECEIVER_EMAIL = "bajjuriani@gmail.com"

msg = EmailMessage()
msg["From"] = SENDER_EMAIL
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = "Test Email from Python"
msg.set_content("Hello! This is my first email sent using Python.")

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()              
    server.login(SENDER_EMAIL, APP_PASSWORD)
    server.send_message(msg)

print("Email sent successfully!")
