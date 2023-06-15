from rest_framework import serializers

from .models import Teacher, Adminstrator, Accountant, Boss

from main.serializers import UserSerializer
from study.serializers import GroupSerializer, ScheduleSerializer

# serializers here

class BossesSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Boss
        filds = ('id', 'user_data', 'is_active', 'salary', 'created_at')
    

class BossDetail(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Boss
        filds = ('id', 'user_data', 'is_active', 'salary', 'created_at')
    
    
class AdminstratorsSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Adminstrator
        filds = ('id', 'user_data', 'is_active', 'salary', 'created_at')


class AdminstratorDetailSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Adminstrator
        filds = ('id', 'user_data', 'is_active', 'salary', 'created_at')


class AccountantsSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Accountant
        filds = ('id', 'user_data', 'is_active', 'salary', 'created_at')
    
    
class AccountantDetailSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Accountant
        filds = ('id', 'user_data', 'is_active', 'salary', 'created_at')
        
    
class TeachersSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Teacher
        filds = ('id', 'user_data', 'is_active', 'salary', 'subjects', 'created_at')
        

class TeacherDetailSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    all_groups = serializers.SerializerMethodField()
    all_groups = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        filds = ('id', 'user_data', 'is_active', 'salary', 'subjects', 'created_at', 
                 'all_groups', 'all_schedules')
        
    def get_all_groups(self, obj):
        groups = obj.get_all_groups()
        return GroupSerializer(groups, many=True, read_only=True).data

    def get_all_schedules(self, obj):
        schedules = obj.get_all_schedules()
        return ScheduleSerializer(schedules, many=True, read_only=True).data
    

