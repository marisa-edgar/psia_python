# Generated by Django 4.0.4 on 2022-05-19 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psia_python_app', '0008_remove_userpost_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
