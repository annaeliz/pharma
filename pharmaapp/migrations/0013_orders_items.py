# Generated by Django 3.2.6 on 2021-08-25 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmaapp', '0012_orders_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='items',
            field=models.ManyToManyField(to='pharmaapp.OrderItem'),
        ),
    ]
