from django.urls import path, include
from rest_framework.routers import DefaultRouter
from network_app.api.views import PostListView, CreatePost, DetailPostView, CommentPostList, CommentDetail, CommentCreate, RatingCreate, LikeComment, TopImageRating


router = DefaultRouter()
#router.register('posts', PostListView, basename='network')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/', CreatePost.as_view(), name='create_post'), 
    path('posts/<int:pk>/', DetailPostView.as_view(), name='detail_post'),
    path('posts/<int:pk>/comments/', CommentPostList.as_view(), name='comments'),
    path('posts/<int:pk>/comments/detail/', CommentDetail.as_view(), name='detail_comment'),
    path('posts/<int:pk>/comments/create/', CommentCreate.as_view(), name='create_comment'),
    path('posts/rating/add/', RatingCreate.as_view(), name='add_rating'),
    path('posts/comments/likes/', LikeComment.as_view(), name='like_comment'),
    path('posts/top10/', TopImageRating.as_view(), name='top10'),
]

