from django.contrib import admin

from .models import Client, Order, Product


class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email", "phone")
    list_filter = ("name", "email", "phone")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image")
    search_fields = (
        "name",
        "price",
    )
    list_filter = (
        "name",
        "price",
    )


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "client",
        "amount",
        "creation_time",
        "order_status",
        "payment_status",
    )
    search_fields = (
        "client",
        "amount",
        "creation_time",
        "order_status",
        "payment_status",
    )
    list_filter = (
        "client",
        "amount",
        "creation_time",
        "order_status",
        "payment_status",
    )


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
