from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import serializers, status
from apps.shop_app.models import Product
from .serializers import ProductSerializer


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "all_products": "/",
        "Search by name": "/?name=product_name",
        "Add": "/create",
        "Update": "/update/pk/",
        "Delete": "/item/pk/delete",
    }
    return Response(api_urls)


@api_view(["POST"])
def add_product(request):
    product = ProductSerializer(data=request.data)

    if Product.objects.filter(**request.data).exists():
        raise serializers.ValidationError("Item already exists")
    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(product.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def all_products(request):
    if request.query_params:
        products = Product.objects.filter(**request.query_params.dict())
    else:
        products = Product.objects.all()
    if products:
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response("No products found", status=status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def update_product(request, pk):
    product = Product.objects.get(pk=pk)
    data = ProductSerializer(product, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return Response("Item deleted successfully", status=status.HTTP_202_ACCEPTED)
