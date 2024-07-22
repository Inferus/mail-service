from fastapi import APIRouter, BackgroundTasks
from .models import EmailSchema
from .service import send_email
from .logger import logger

router = APIRouter()

@router.post("/emails")
async def send_email_endpoint(email: EmailSchema, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email)
    logger.info(f"Received request to send email to {email.email}")
    return {"message": "Email has been sent"}
