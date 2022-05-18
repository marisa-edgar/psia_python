# Generated by Django 4.0.4 on 2022-05-18 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psia_python_app', '0003_imagepost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='image',
        ),
        migrations.AddField(
            model_name='userpost',
            name='image',
            field=models.ImageField(blank=True, upload_to='files/images'),
        ),
    ]