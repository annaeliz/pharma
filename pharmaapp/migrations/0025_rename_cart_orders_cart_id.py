# Generated by Django 3.2.6 on 2021-08-28 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmaapp', '0024_alter_orders_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='cart',
            new_name='cart_id',
        ),
    ]