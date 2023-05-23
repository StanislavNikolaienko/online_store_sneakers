from apps.shop_app.rapidapi.sneakers_db_update import update_db
from celery import shared_task


@shared_task
def update_sneakers_db(data):
    update_db(data)
