from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Group, Schedule
from .serializers import GroupSerializer, GroupDetailSerializer
from .schedule_serializers import ScheduleSerializer, ScheduleDetailSerializer

class GroupViewSet(generics.ListCreateAPIView):
    queryset = Group.objects.select_related('teacher__user').prefetch_related('schedule_set', 'student_set').all()
    serializer_class = GroupSerializer
    

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.queryset = Group.objects.select_related('teacher__user')
    serializer_class = GroupDetailSerializer
    
    
class ScheduleView(generics.ListCreateAPIView):
    queryset = Schedule.objects.select_related('group', 'room').all()
    serializer_class = ScheduleSerializer
    

class ScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.select_related('group', 'room').all()
    serializer_class = ScheduleDetailSerializer
    
    
    