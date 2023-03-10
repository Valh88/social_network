# Generated by Django 4.1.5 on 2023-01-31 09:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0004_remove_profile_following_userfollowing'),
        ('network_app', '0003_alter_post_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='network_app.post')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts_app.profile')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='rates',
            field=models.ManyToManyField(through='network_app.Rating', to='accounts_app.profile'),
        ),
    ]
