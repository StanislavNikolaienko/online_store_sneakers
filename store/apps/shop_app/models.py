from django.db import models


class OrderStatus(models.TextChoices):
    PENDING = "PENDING", "PENDING"
    APPROVED = "APPROVED", "APPROVED"
    REJECTED = "REJECTED", "REJECTED"
    CANCELED = "CANCELED", "CANCELED"
    DELIVERED = "DELIVERED", "DELIVERED"


class PaymentStatus(models.TextChoices):
    WAITING_PAYMENT = "Waiting Payment", "Waiting Payment"
    PAID = "Paid", "Paid"
    CANCELED = "Canceled", "Canceled"


class PaymentMethod(models.TextChoices):
    CASH = "Cash", "Cash"
    CARD = "Card", "Card"


class Payment(models.Model):
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=50, choices=PaymentMethod.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payment_method


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    comment = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    token_product = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    creation_time = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, choices=OrderStatus.choices)
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices)
    comment = models.TextField(blank=True, null=True)
