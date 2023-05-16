from django.urls import path

from .views.clients import ClientCreate
from .views.products import (
    ProductListCreateView,
    ProductRetrieveUpdateDestroy,
)


urlpatterns = [
    path("sneakers/", ProductListCreateView.as_view(), name="list_create_products"),
    path(
        "sneakers/<int:pk>/",
        ProductRetrieveUpdateDestroy.as_view(),
        name="update_product",
    ),
    path(
        "sneakers/<int:pk>/",
        ProductRetrieveUpdateDestroy.as_view(),
        name="delete_product",
    ),
    path("clients/", ClientCreate.as_view(), name="add_client"),
]
