# Generated by Django 5.0.2 on 2024-02-24 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0014_chicken1_lat_chicken1_lon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chicken1',
            name='lat',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
        migrations.AlterField(
            model_name='chicken1',
            name='lon',
            field=models.DecimalField(decimal_places=7, max_digits=10),
        ),
    ]
