# Generated by Django 2.1.4 on 2018-12-19 13:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_restaurantlocation_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocation',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
