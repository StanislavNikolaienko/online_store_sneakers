# Generated by Django 4.2 on 2023-05-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop_app", "0002_alter_product_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="payment_method",
            field=models.CharField(
                choices=[("Cash", "Cash"), ("Card", "Card")], max_length=50
            ),
        ),
    ]
