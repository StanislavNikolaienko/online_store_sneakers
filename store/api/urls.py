from django.urls import path

from .views.clients import ClientCreate
from .views.products import (
    ProductListView,
    ProductCreateView,
    ProductRetrieveUpdateDestroy,
)


urlpatterns = [
    path("sneakers/", ProductListView.as_view(), name="all_products"),
    path("sneakers/", ProductCreateView.as_view(), name="add_product"),
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
