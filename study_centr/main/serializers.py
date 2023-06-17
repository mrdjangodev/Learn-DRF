from django.utils import timezone

from rest_framework import serializers

from .models import CustomUser, Room, Subject
from study.models import Schedule
from study.serializers import GroupSerializer 
from study.schedule_serializers import ScheduleSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        

class SubjectDetailSerializer(serializers.ModelSerializer):
    all_groups = serializers.SerializerMethodField('get_all_groups')
    class Meta:
        model = Room
        fields = ('id', 'name', 'all_groups')

    def get_all_groups(self, obj):
        groups = obj.get_all_groups()
        return GroupSerializer(groups, many=True).data
        

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RoomDetailSerializer(serializers.ModelSerializer):
    all_schedules = serializers.SerializerMethodField()
    daily_schedules = serializers.SerializerMethodField()
    future_schedules = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = ('id', 'name', 'all_schedules', 'daily_schedules', 'future_schedules')

    def get_all_schedules(self, obj):
        schedules = obj.get_all_schedules()
        return ScheduleSerializer(schedules, many=True).data

    def get_daily_schedules(self, obj):
        today = timezone.now().date()
        schedules = Schedule.objects.filter(room=obj, start_time__date=today)
        return ScheduleSerializer(schedules, many=True).data

    def get_future_schedules(self, obj):
        today = timezone.now().date()
        schedules = Schedule.objects.filter(room=obj, start_time__date__gte=today)
        return ScheduleSerializer(schedules, many=True).data