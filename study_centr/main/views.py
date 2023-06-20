from django.contrib.auth import authenticate
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from dj_rest_auth.serializers import LoginSerializer


from .models import CustomUser, Subject, Room
from .user_serializers import UserDetailSerializer, UserSerializer, SignUpSerializer
from .serializers import (
    RoomSerializer, RoomDetailSerializer, 
    SubjectSerializer, SubjectDetailSerializer)


# Create your views here.
class SignUpView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    
    def post(self, request: Request):
        data = request.data
        
        serializer = self.serializer_class(data=data)
        
        if serializer.is_valid():
            serializer.save()
            response = {"message": "User created Successfully", 'data': serializer.data}
            
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(generics.GenericAPIView):
    permission_classes = []
    serializer_class = LoginSerializer
    
    def post(self, request: Request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            response = {'message': "Logged In Successfully",
                        "token": str(user.auth_token),
                        }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"Invalid Email or Password"}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request: Request):
        contex = {
            'user': str(request.user), 
            'auth': str(request.auth),
        }
        return Response(data=contex, status=status.HTTP_200_OK)

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
    queryset = Subject.objects.all()
    serializer_class = SubjectDetailSerializer
