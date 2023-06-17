from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import CustomUser, Subject, Room
from .user_serializers import UserDetailSerializer, UserSerializer
from .serializers import (
    RoomSerializer, RoomDetailSerializer, 
    SubjectSerializer, SubjectDetailSerializer)


# Create your views here.

class UserViewSet(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
    
    
class UserDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
   
   
class RoomViewSet(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
   

class RoomDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    # queryset = Room.objects.prefetch_related('schedule')
    serializer_class = RoomDetailSerializer
   
   
class SubjectViewSet(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
   

class SubjectDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.prefetch_related('group')
    serializer_class = SubjectDetailSerializer
