from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate 

class UserRegisterSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    first_name=serializers.CharField()
    last_name=serializers.CharField()



    def validate(self,data):
        # data is a python dictionary to validate the serializer
        # It is one of the form of object level validation --> 1) Field level vaildation 2) object level 3) validator
        
        username=data['username']
        try:
            if User.objects.get(username=username).exists():
                raise serializers.ValidationError("Username already exist")
        except:
            return data

    
    # since I am using serializers.Serializer then i have to create create and update function

    def create(self, validated_data):
        user=User.objects.create(
            username=validated_data['username'].lower(),
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


    def validate(self,data):
        # check user with that name exist or not
        if not User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("User not found")
        return data
    
    def get_tokens_for_user(self, data):
        user= authenticate(username=data['username'],password=data['password'])
        print(user)

        if not user:
            return {'message':'invalid credentials','data':{}}
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }