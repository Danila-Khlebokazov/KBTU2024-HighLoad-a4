import time

from .models import EmailMessage
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from logging import getLogger

logger = getLogger(__name__)


def send_email_message(message: EmailMessage) -> bool:
    # Send the email message
    send_mail(
        message.subject,
        message.body,
        settings.EMAIL_HOST_USER,
        [message.recipient.email],
        fail_silently=False,
    )

    logger.info(f"Email message sent: {message.id}")

    return True
