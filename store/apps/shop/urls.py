from django.urls import path
from .views import about, contact
from . import views

urlpatterns = [
 path('', views.all_items, name='all_items'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
