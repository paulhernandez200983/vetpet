# Generated by Django 5.0.2 on 2024-02-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0022_remove_userprofile_profile_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
