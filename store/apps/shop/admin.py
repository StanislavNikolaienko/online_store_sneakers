from django.contrib import admin
from .models import Client, Product, Order, OrderDetail

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email', 'phone', 'address')
    list_filter = ('name', 'email', 'phone', 'address')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name', 'price', 'stock')
    list_filter = ('name', 'price', 'stock')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'amount', 'creation_time', 'order_status', 'payment_status')
    search_fields = ('client', 'amount', 'creation_time', 'order_status', 'payment_status')
    list_filter = ('client', 'amount', 'creation_time', 'order_status', 'payment_status')

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'product', 'quantity', 'price', 'discount')
    search_fields = ('order_id', 'product', 'quantity', 'price', 'discount')
    list_filter = ('order_id', 'product', 'quantity', 'price', 'discount')

