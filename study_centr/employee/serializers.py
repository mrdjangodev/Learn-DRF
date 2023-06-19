from django.db.models import Q
from rest_framework import serializers

from .models import Teacher, Adminstrator, Accountant, Boss

from main.user_serializers import UserSerializer
from study.serializers import GroupSerializer
from study.schedule_serializers import ScheduleSerializer
from main.serializers import SubjectSerializer
from .models import CustomUser
# serializers here

class BossesSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    class Meta:
        model = Boss
        fields = ('id', 'user_data', 'is_active', 'salary', 'created_at')
        
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        boss = Boss.objects.create(user=user, **validated_data)
        return boss   


class BossDetailSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Boss
        fields = ('id', 'user_data', 'is_active', 'salary', 'created_at')
    
    
# class AdminstratorsSerializer(serializers.ModelSerializer):
#     user_data = UserSerializer(source='user')
#     class Meta:
#         model = Adminstrator
#         fields = ('id', 'user_data', 'is_active', 'salary', 'created_at')
    
#     def create(self, validated_data):
#         user_data = validated_data.pop('user')
#         user = CustomUser.objects.create(**user_data)
#         adminstrator = Adminstrator.objects.create(user=user, **validated_data)
#         return adminstrator   

# class AdminstratorDetailSerializer(serializers.ModelSerializer):
#     user_data = UserSerializer(source='user', read_only=True)
#     class Meta:
#         model = Adminstrator
#         fields = ('id', 'user_data', 'is_active', 'salary', 'created_at')


class AccountantsSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    class Meta: 
        model = Accountant
        fields = ('id', 'user_data', 'is_active', 'salary', 'created_at')
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        accountant = Accountant.objects.create(user=user, **validated_data)
        return accountant   
    
class AccountantDetailSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Accountant
        fields = ('id', 'user_data', 'is_active', 'salary', 'created_at')
    


class TeachersSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')

    class Meta:
        model = Teacher
        fields = ('id', 'user_data', 'is_active', 'salary', 'subjects', 'created_at')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        subjects = validated_data.pop('subjects', [])
        teacher = Teacher.objects.create(user=user, **validated_data)
        teacher.subjects.set(subjects)
        return teacher
    

class TeacherDetailSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', required=False, read_only=True)
    all_groups = serializers.SerializerMethodField('get_all_groups')
    all_schedules = serializers.SerializerMethodField('get_all_schedules')
    class Meta:
        model = Teacher
        fields = ('id', 'user_data', 'is_active', 'salary', 'subjects', 'created_at', 
                 'all_groups', 'all_schedules')
        
    def get_all_groups(self, obj):
        groups = obj.get_all_groups()
        return GroupSerializer(groups, many=True, read_only=True).data

    def get_all_schedules(self, obj):
        schedules = obj.get_all_schedules()
        return ScheduleSerializer(schedules, many=True, read_only=True).data
    
   