# Generated by Django 3.2.6 on 2021-08-31 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmaapp', '0028_remove_orders_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='quantity',
        ),
    ]