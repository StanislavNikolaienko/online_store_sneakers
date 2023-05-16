from rest_framework import generics

from api.serializers.product import ProductSerializer
from apps.shop_app.models import Product


class ProductListView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductCreateView(generics.CreateAPIView):
    model = Product
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
