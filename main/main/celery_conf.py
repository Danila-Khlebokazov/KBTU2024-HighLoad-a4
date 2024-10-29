import os

import celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

celery_app = celery.Celery(broker="redis://redis:6379")

celery_app.config_from_object("django.conf:settings", namespace="CELERY")

celery_app.autodiscover_tasks()

celery_app.conf.beat_schedule = {
    'audit-logs-every-day': {
        'task': 'tasks.tasks.audit_logs',
        'schedule': crontab(minute="*/5"),
    },
}
