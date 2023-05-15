from django.urls import path
from . import views


urlpatterns = [
    path("", views.apiOverview, name="home"),
    path("api/sneakers/", views.add_product, name="add_product"),
    path("api/sneakers/all/", views.all_products, name="all-products"),
    path("api/sneakers/<int:pk>/", views.update_product, name="update-product"),
    path("api/sneakers/<int:pk>/", views.delete_product, name="delete-product"),
    path("api/clients/", views.add_client, name="add_client"),
]
