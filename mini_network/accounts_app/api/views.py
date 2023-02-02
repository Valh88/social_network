from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserFollowingSerializer, RegistrationSerializer, ProfileForFullSerializer
from rest_framework.response import Response
from accounts_app.models import Profile, UserFollowing
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view


class UserListView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        users = User.objects.all()
        ser =  UserSerializer(users, many=True, read_only=True, context= {'request': request})
        return Response(ser.data, status=status.HTTP_200_OK) 


class FollowingUser(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(id=request.user.id)
        following = profile.following.all()
        ser = UserFollowingSerializer(following, many=True, read_only=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class Following(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user_to_follow = Profile.objects.get(pk=pk)
        ser =  ProfileForFullSerializer(user_to_follow, read_only=True, context= {'request': request})
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        user_to_follow = Profile.objects.get(pk=pk)
        user = request.user.profile
        try:
            follow  = UserFollowing.objects.get(user_id=user, follower=user_to_follow)
        except UserFollowing.DoesNotExist:
            user.following.create(user_id=user, follower=user_to_follow)
            return Response({"status": "successfull"}, status=status.HTTP_200_OK)
        return Response({"error": "you are following!"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        user_to_follow = Profile.objects.get(pk=pk)
        user = request.user.profile
        try:
            follow  = UserFollowing.objects.get(user_id=user, follower=user_to_follow)
            follow.delete()
            return Response({"status": "successfull"}, status=status.HTTP_200_OK)
        except UserFollowing.DoesNotExist:
            return Response({"error": "you are not following!"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration Successful! You can login!"
            data['username'] = account.username
            data['email'] = account.email
            # token = Token.objects.create(user=account).key       
            # data['token'] = token
       
        else:
            data = serializer.errors
        
        return Response(data, status=status.HTTP_201_CREATED)


@api_view(['POST',])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)