from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.shop_app.models import Product, Client

import mock


class ClientTests(APITestCase):
    def test_create_client(self):
        """
        Ensure we can create a new client object.
        """
        url = reverse("add_client")
        data = {
            "name": "John",
            "email": "asdw@adaw.com",
            "phone": "123134",
            "comment": "asdaaw",
        }
        response = self.client.post(url, data, format="json")
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, "John")
        self.assertEqual(Client.objects.get().email, "asdw@adaw.com")
        self.assertEqual(Client.objects.get().phone, "123134")
        self.assertEqual(Client.objects.get().comment, "asdaaw")


class ProductTests(APITestCase):
    @mock.patch("apps.shop_app.models.Product.objects")
    def test_all_products(self, mock_products):
        """
        Ensure we can get all products.
        """
        url = reverse("all-products")
        mock_products.all.return_value = [
            Product(name="product_1", price=110.00),
            Product(name="product_2", price=120.00),
        ]
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        self.assertEqual(
            response.data,
            [
                {"name": "product_1", "price": "110.00"},
                {"name": "product_2", "price": "120.00"},
            ],
        )
