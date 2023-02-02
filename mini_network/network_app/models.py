from django.db import models
from accounts_app.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator


def user_directory_path(instance, image_name):
    return f'users/{instance.publisher.user.username}/{image_name}'


class Post(models.Model):
    img = models.ImageField(upload_to=user_directory_path)
    publisher  = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)
    rates = models.ManyToManyField(Profile, through='Rating')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='create data')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='update data')


class Comment(models.Model):
    commentator = models.ForeignKey(Profile, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='create data')


class Rating(models.Model):
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
