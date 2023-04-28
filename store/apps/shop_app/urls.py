from django.urls import path

from .views import Index, item_detail

urlpatterns = [
    path("item/<int:item_id>/", item_detail, name="item_detail"),
    path("", Index.as_view()),
]
