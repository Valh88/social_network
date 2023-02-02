from django.urls import path, include
from rest_framework.routers import DefaultRouter
from network_app.api.views import PostListView, CreatePost, DetailPostView, CommentPostList, CommentDetail, CommentCreate


router = DefaultRouter()
#router.register('posts', PostListView, basename='network')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/', CreatePost.as_view(), name='create_post'), 
    path('posts/<int:pk>/', DetailPostView.as_view(), name='detail_post'),
    path('posts/<int:pk>/comments/', CommentPostList.as_view(), name='comments'),
    path('posts/comments/<int:pk>/detail/', CommentDetail.as_view(), name='detail_comment'),
    path('posts/<int:pk>/comments/create/', CommentCreate.as_view(), name='create_comment'),
]

