from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.schemas.contact import ContactRequest
from app.services.email_service import send_contact_email
from app.core.config import settings

router = APIRouter()

@router.post("/")
async def send_contact_message(contact: ContactRequest):
    """
    Handle contact form submission. 
    """
    if not settings.SMTP_USER or not settings.SMTP_PASSWORD:
        raise HTTPException(
            status_code=500, 
            detail="Email service not configured."
        )

    try:
        await send_contact_email(
            name=contact.name,
            email=contact.email,
            message=contact.message,
            to_email=settings.SMTP_USER
        )
    except Exception as e:
        print(f"EMAIL ERROR: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
    
    return {"message": "Message sent successfully!"}
