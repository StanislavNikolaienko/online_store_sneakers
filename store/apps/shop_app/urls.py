from django.urls import path
from .views import  item_detail, Index

urlpatterns = [
    path('item/<int:item_id>/', item_detail, name='item_detail'),
    path('', Index.as_view())
]
