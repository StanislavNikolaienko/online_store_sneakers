from django.urls import path
from . import views


urlpatterns = [
    path("", views.apiOverview, name="home"),
    path("create/", views.add_product, name="add-product"),
    path("all/", views.all_products, name="all-products"),
    path("update/<int:pk>/", views.update_product, name="update-product"),
    path("delete/<int:pk>/", views.delete_product, name="delete-product"),
]
