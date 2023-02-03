from rest_framework import serializers
from network_app.models import Post, Comment, Rating, CommentLikes
from accounts_app.models import Profile
from accounts_app.api.serializers import ProfileFullSerializer, ProfileSerializer


class CommentForPostFullSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('comment')


class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = ('rate', 'post',)


class PostSerializer(serializers.ModelSerializer):
    # url = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    publisher = ProfileSerializer(read_only=True)
    # comments = CommentForPostFullSerializer(many=True, read_only=True)
    # rates = RatingSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = ('id', 'publisher', 'img', 'created_at', 'updated_at', 'average_rating',)


class DetailPostSerializer(serializers.ModelSerializer):
    publisher = ProfileSerializer(read_only=True)
    # rates = RatingSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = ('id', 'publisher', 'img', 'created_at', 'updated_at', 'average_rating',)


class CreatePostSerializer(serializers.Serializer):   
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)


class CommentSerializer(serializers.ModelSerializer):
    commentator = ProfileSerializer(read_only=True)
    # post = DetailPostSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'commentator', 'comment', 'like_count', 'created_at',)


class LikeCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentLikes
        fields = ('comment',)
    