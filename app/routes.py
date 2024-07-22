from fastapi import APIRouter
from .models import EmailSchema
from .service import send_email
from .logger import logger

router = APIRouter()

@router.post("/emails")
async def send_email_endpoint(email: EmailSchema):
    send_email(email)
    logger.info(f"Received request to send email to {email.email}")
    return {"message": "Email has been sent"}
