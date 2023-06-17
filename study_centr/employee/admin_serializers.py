from rest_framework import serializers
from .models import Adminstrator

from main.user_serializers import UserSerializer

class AdminstratorsSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    class Meta:
        model = Adminstrator
        fields = ('id', 'user_data', 'is_active', 'salary', 'created_at')


class AdminstratorDetailSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Adminstrator
        fields = ('id', 'user_data', 'is_active', 'salary', 'created_at')