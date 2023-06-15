from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Group
from .serializers import GroupSerializer

class GroupViewSet(generics.ListCreateAPIView):
    queryset = Group.objects.select_related('teacher__user').prefetch_related('schedule_set', 'student_set').all()
    serializer_class = GroupSerializer
    
    # def list(self, request):
    #     # Your list implementation here
    #     return Response({'message': 'List of users'})