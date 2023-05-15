from rest_framework import serializers
from apps.shop_app.models import Product, Client


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "price")


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("name", "email", "phone", "comment")
