from utils.sneakers_db_update import update_db
from celery import shared_task


@shared_task
def update_sneakers_db():
    update_db()
