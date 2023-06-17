from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Group
from .serializers import GroupSerializer, GroupDetailSerializer

class GroupViewSet(generics.ListCreateAPIView):
    queryset = Group.objects.select_related('teacher__user').prefetch_related('schedule_set', 'student_set').all()
    serializer_class = GroupSerializer
    

class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.queryset = Group.objects.select_related('teacher__user')
    serializer_class = GroupDetailSerializer