import os
from django.core.exceptions import MultipleObjectsReturned
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.config.settings")
django.setup()

from apps.shop_app.models import Product
from apps.shop_app.rapidapi.receive_data import get_sneakers


def update_db(data: dict):
    for sneaker_data in data:
        try:
            sneaker, created = Product.objects.update_or_create(
                token_product=sneaker_data["id"],
                defaults={
                    "image": sneaker_data["image"]["small"],
                    "name": sneaker_data["name"],
                    "price": sneaker_data["retailPrice"],
                    "description": sneaker_data["story"],
                },
            )
            if created:
                print(f"Created new sneaker: {sneaker.name}")
            else:
                print(f"Updated existing sneaker: {sneaker.name}")
        except MultipleObjectsReturned:
            print(
                "Multiple products found with the same token_product:"
                f" {sneaker_data['id']}"
            )


api_data = get_sneakers()["results"]
update_db(api_data)
