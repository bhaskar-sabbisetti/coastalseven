import asyncio
import os
from dotenv import load_dotenv
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType

# Force reload of .env
load_dotenv(override=True)

print("--- Testing Email Configuration ---")
username = os.getenv("SMTP_USER")
password = os.getenv("SMTP_PASSWORD")
print(f"User: {username}")
print(f"Password Length: {len(password) if password else 0}")
print(f"Port: {os.getenv('SMTP_PORT')}")

conf = ConnectionConfig(
    MAIL_USERNAME=username,
    MAIL_PASSWORD=password,
    MAIL_FROM=username,
    MAIL_PORT=int(os.getenv("SMTP_PORT", 587)),
    MAIL_SERVER=os.getenv("SMTP_HOST", "smtp.gmail.com"),
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=False 
)

async def test_send():
    print("Attempting to connect...")
    message = MessageSchema(
        subject="Test Email",
        recipients=[username],
        body="This is a test email.",
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    try:
        await fm.send_message(message)
        print("✅ SUCCESS: Email sent successfully!")
    except Exception as e:
        print(f"❌ FAILED: {e}")

if __name__ == "__main__":
    asyncio.run(test_send())
