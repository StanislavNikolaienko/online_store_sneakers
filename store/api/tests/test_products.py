from _decimal import Decimal

from rest_framework import status
from rest_framework.test import APITestCase
from apps.shop_app.models import Product


class TestProduct(APITestCase):
    def setUp(self):
        Product.objects.create(name="product_1", price="110.00")
        Product.objects.create(name="product_2", price="120.00")

    def test_all_products(self):
        """
        Ensure we can get all products.
        """
        url = "/api/sneakers/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(Product.objects.count(), 2)

    def test_create_product(self):
        """
        Ensure we can create a new product object.
        """
        url = "/api/sneakers/new/"
        data = {"name": "new product", "price": "210.00"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Product.objects.count(), 3)
        self.assertEqual(Product.objects.get(id=response.data["id"]).name, data["name"])
        self.assertEqual(
            Product.objects.get(id=response.data["id"]).price, Decimal(data["price"])
        )
