import os
import django
import requests
from django.core.exceptions import MultipleObjectsReturned

from apps.shop_app.models import Product
from config.settings import XRapidAPIKey, XRapidAPIHost, XRapidAPI_URL

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store.config.settings")
django.setup()


def get_sneakers():
    querystring = {"limit": "100"}
    headers = {
        "X-RapidAPI-Key": f"{XRapidAPIKey}",
        "X-RapidAPI-Host": f"{XRapidAPIHost}",
    }
    response = requests.request(
        "GET", XRapidAPI_URL, headers=headers, params=querystring
    )
    data = response.json()
    return data


def update_db():
    # sneakers = get_sneakers()
    for sneaker_data in get_sneakers()["results"]:
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
