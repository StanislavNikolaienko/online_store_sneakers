# Generated by Django 4.2 on 2023-05-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop_app", "0003_alter_payment_payment_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="token_product",
            field=models.CharField(max_length=254),
        ),
    ]
