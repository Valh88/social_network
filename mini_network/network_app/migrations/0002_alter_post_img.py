# Generated by Django 4.1.5 on 2023-01-31 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(height_field=100, upload_to='images/', width_field=100),
        ),
    ]