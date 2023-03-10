# Generated by Django 4.1.5 on 2023-01-31 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0003_alter_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='following',
        ),
        migrations.CreateModel(
            name='UserFollowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='accounts_app.profile')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='accounts_app.profile')),
            ],
        ),
    ]
