from django.db import models
from accounts_app.models import Profile
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from django.db.models import CheckConstraint, Q, UniqueConstraint


def user_directory_path(instance, image_name):
    return f'users/{instance.publisher.user.username}/{image_name}'


class Post(models.Model):
    img = models.ImageField(upload_to=user_directory_path)
    publisher  = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)
    # rates = models.ManyToManyField('Rating', through='Rating')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='create data')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='update data')

    @property
    def average_rating(self):
        return self.rates.all().aggregate(Avg('rate'))['rate__avg']

    class Meta:
        ordering = ('-created_at',)

class Comment(models.Model):
    commentator = models.ForeignKey(Profile, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='create data')
    
    @property
    def like_count(self):
        return self.likes.all().count()


class Rating(models.Model):
    rate = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='rates')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # class Meta:
        # constraints = [
            # CheckConstraint(check=Q(rate__range=(0, 5)), name='valid_rate'),
            # UniqueConstraint(fields=['profile', 'post'], name='rating_once')
        # ]


class CommentLikes(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')

