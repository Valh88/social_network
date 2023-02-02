from rest_framework import serializers
from network_app.models import Post, Comment
from accounts_app.models import Profile
from accounts_app.api.serializers import ProfileFullSerializer, ProfileSerializer

class PostSerializer(serializers.ModelSerializer):
    # url = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    publisher = ProfileSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'img', 'publisher']


class DetailPostSerializer(serializers.ModelSerializer):
    publisher = ProfileSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'


class CreatePostSerializer(serializers.Serializer):
    
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)


class CommentSerializer(serializers.ModelSerializer):
    commentator = ProfileSerializer(read_only=True)
    # post = DetailPostSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'commentator', 'comment', 'created_at',)