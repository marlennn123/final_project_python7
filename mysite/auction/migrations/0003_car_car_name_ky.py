# Generated by Django 5.0.4 on 2024-05-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_car_car_name_en_car_car_name_ru'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_name_ky',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
