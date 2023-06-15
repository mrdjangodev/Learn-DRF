from rest_framework import viewsets
from .models import Group
from .serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.select_related('teacher__user').prefetch_related('schedule_set', 'student_set').all()
    serializer_class = GroupSerializer