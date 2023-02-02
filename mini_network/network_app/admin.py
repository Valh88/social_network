from django.contrib import admin
from .models import Comment, Post, Rating


class PostAdmin(admin.ModelAdmin):
    list_display = ['publisher', 'created_at', 'updated_at']



class CommentAdmin(admin.ModelAdmin):
    list_display = ['commentator', 'post', 'comment']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['rate', 'post', 'profile']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Rating, RatingAdmin)
