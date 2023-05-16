from rest_framework import generics

from api.serializers.clients import ClientSerializer
from apps.shop_app.models import Client


class ClientCreate(generics.CreateAPIView):
    model = Client
    serializer_class = ClientSerializer
