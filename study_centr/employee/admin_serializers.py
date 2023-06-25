from rest_framework import serializers

from .models import Adminstrator
from main.models import CustomUser

from main.user_serializers import UserSerializer

class AdminstratorsSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    password = serializers.CharField(max_length=184, write_only=True)
    class Meta:
        model = Adminstrator
        fields = ('id', 'user_data', 'password', 'is_active', 'salary', 'created_at')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        user.set_password(validated_data.pop('password'))
        adminstrator = Adminstrator.objects.create(user=user, **validated_data)
        return adminstrator   

class AdminstratorDetailSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Adminstrator
        fields = ('id', 'user_data', 'is_active', 'salary', 'created_at')