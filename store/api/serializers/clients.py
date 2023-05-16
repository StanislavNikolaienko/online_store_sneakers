from rest_framework import serializers
from apps.shop_app.models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("name", "email", "phone", "comment")
