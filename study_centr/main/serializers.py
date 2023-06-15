from rest_framework import serializers

from .models import CustomUser, Room, Subject


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'phone')


class SubjectSerializer(serializers.ModelSerializer):
    model = Subject
    fields = ('id', 'name')