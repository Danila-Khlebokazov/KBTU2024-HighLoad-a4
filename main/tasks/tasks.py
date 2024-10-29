import os
import re

from django.utils import timezone

import celery

from django.conf import settings
from .services import send_email_message
from .models import EmailMessage
from logging import getLogger

logger = getLogger(__name__)


@celery.shared_task(bind=True, max_retries=3)
def send_email_message_task(self, message_id: int):
    try:
        message = EmailMessage.objects.get(pk=message_id)
        send_email_message(message)
        message.sent_at = timezone.now()
        message.save()
    except Exception as e:
        self.retry(exc=e, countdown=60)


@celery.shared_task
def audit_logs():
    log_file_path = os.path.join(settings.BASE_DIR, 'logs', 'django_info.log')
    error_pattern = re.compile(r'ERROR|CRITICAL')

    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                if error_pattern.search(line):
                    logger.warning(f"Suspicious log entry found: {line}")
    except FileNotFoundError:
        logger.error("Log file not found during audit.")
