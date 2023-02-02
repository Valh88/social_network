from django.contrib import admin
from .models import Profile, UserFollowing


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id']


class UserFollowingAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserFollowing, UserFollowingAdmin)

