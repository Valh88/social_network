from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # following = models.ManyToManyField("self", related_name="followers", symmetrical=False, blank=True)


class UserFollowing(models.Model):
    user_id = models.ForeignKey(Profile, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(Profile, related_name='followers', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_id','follower'],  name="unique_followers")
        ]

        ordering = ["-created"]


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
