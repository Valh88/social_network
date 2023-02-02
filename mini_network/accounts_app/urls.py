from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts_app.api.views import UserListView, FollowingUser, Following, registration_view, logout_view
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
#router.register('posts', PostListView, basename='network')

urlpatterns = [
    path('users/', UserListView.as_view(), name='users_list'),
    path('users/follow/', FollowingUser.as_view(), name='user_list'),
    path('users/<int:pk>/follow/', Following.as_view(), name='follow_unfollow'),
    path('users/login/', obtain_auth_token, name='token_login'),
    path('users/register/', registration_view, name='register'),
    path('users/logout/', logout_view, name='logout'),

]


