# Generated by Django 5.0.2 on 2024-02-29 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0023_remove_customuser_profile_picture_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='estado',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
