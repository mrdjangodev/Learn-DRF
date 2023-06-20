from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import ValidationError

from .models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'password')

    def validate(self, attrs):
        email_exists = CustomUser.objects.filter(email=attrs['email']).exists()
        username_exists = CustomUser.objects.filter(username=attrs['username']).exists()
        if email_exists:
            raise ValidationError("Email has already been taken")
        elif username_exists:
            raise ValidationError("Username has already been taken")
        return super().validate(attrs)
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ('email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone')
        

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone', 'created_at', 'updated_at')

        