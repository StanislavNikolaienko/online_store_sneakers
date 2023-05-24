from apps.shop_app.rapidapi.receive_data import get_sneakers
from apps.shop_app.rapidapi.sneakers_db_update import update_db
from celery import shared_task


@shared_task
def update_sneakers_db():
    api_data = get_sneakers()["results"]
    update_db(api_data)
