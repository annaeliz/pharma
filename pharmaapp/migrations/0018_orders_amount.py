# Generated by Django 3.2.6 on 2021-08-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmaapp', '0017_alter_carts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]