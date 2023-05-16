from rest_framework import status
from rest_framework.test import APITestCase
from apps.shop_app.models import Client


class TestClient(APITestCase):
    def test_create_client(self):
        """
        Ensure we can create a new client object.
        """
        url = "/api/clients/new/"
        data = {
            "name": "John",
            "email": "asdw@adaw.com",
            "phone": "123134",
            "comment": "asdaaw",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, "John")
        self.assertEqual(Client.objects.get().email, "asdw@adaw.com")
        self.assertEqual(Client.objects.get().phone, "123134")
        self.assertEqual(Client.objects.get().comment, "asdaaw")
