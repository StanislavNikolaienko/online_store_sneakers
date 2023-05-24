import os
from celery import Celery
from celery.schedules import crontab
from .settings import CELERY_BROKER_URL


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


app = Celery("config", broker=CELERY_BROKER_URL)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "update-sneakers-every-2-minute": {
        "task": "api.tasks.update_sneakers_db",
        "schedule": crontab(minute="*/2"),
    },
}
