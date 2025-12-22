from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from app.core.config import settings
from typing import List

# Configure SMTP Connection
conf = ConnectionConfig(
    MAIL_USERNAME=settings.SMTP_USER,
    MAIL_PASSWORD=settings.SMTP_PASSWORD,
    MAIL_FROM=settings.EMAILS_FROM_EMAIL or settings.SMTP_USER,
    MAIL_PORT=465, # Force SSL Port
    MAIL_SERVER=settings.SMTP_HOST,
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True 
)

async def send_contact_email(name: str, email: str, message: str, to_email: str):
    """
    Sends a contact form email to the site owner.
    """
    subject = f"Portfolio Contact: {name}"
    
    html = f"""
    <h3>New Contact Message</h3>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Email:</strong> {email}</p>
    <p><strong>Message:</strong></p>
    <p>{message}</p>
    """

    message = MessageSchema(
        subject=subject,
        recipients=[to_email],
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)
