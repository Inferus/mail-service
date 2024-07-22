import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import HTTPException
from .models import EmailSchema
from .config import settings
from .logger import logger

def send_email(email: EmailSchema):
    try:
        msg = MIMEMultipart()
        msg['From'] = settings.SMTP_USERNAME
        msg['To'] = email.email
        msg['Subject'] = email.subject

        msg.attach(MIMEText(email.message, 'plain'))

        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.starttls()
            server.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
            server.sendmail(settings.SMTP_USERNAME, email.email, msg.as_string())

        logger.info(f"Email sent to {email.email}")

    except Exception as e:
        logger.error(f"Failed to send email to {email.email}. Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to send email")
