# Generated by Django 4.2.1 on 2023-06-05 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CART', '0004_order_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Totalprice',
            field=models.IntegerField(),
        ),
    ]
