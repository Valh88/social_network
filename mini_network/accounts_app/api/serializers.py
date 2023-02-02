from rest_framework import serializers
from accounts_app.models import Profile, UserFollowing
from django.contrib.auth.models import User


class UserFollowingSerializer(serializers.ModelSerializer):
    # follower = ProfileSerializer(read_only=True)

    class Meta:
        model = UserFollowing
        fields = ('id', 'follower', 'created',)



class ProfileSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = ['id'] 


class ProfileForFullSerializer(serializers.ModelSerializer):
    followers = UserFollowingSerializer(many=True, read_only=True)
    following = UserFollowingSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('id', 'followers', 'following')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileForFullSerializer(read_only=True)

    class Meta: 
        model = User
        fields = ['id','username', 'profile'] 



class ProfileFullSerializer(serializers.ModelSerializer):
    followers = ProfileSerializer(many=True, read_only=True)
    following = ProfileSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ('id', 'followers', 'following')


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only': True}
        }
    
    def save(self):
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'P1 and P2 should be same!'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Email already exists!'})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'])
        account.set_password(password)
        account.save()

        return account


