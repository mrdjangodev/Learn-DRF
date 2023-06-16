from rest_framework.generics import (ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView)

from .models import Teacher, Accountant, Adminstrator, Boss
from .serializers import (TeachersSerializer, TeacherDetailSerializer, 
                          AccountantsSerializer, AccountantDetailSerializer,
                          AdminstratorsSerializer, AdminstratorDetailSerializer, 
                          BossesSerializer, BossDetailSerializer,)
# Create your views here.

class BossesListView(ListAPIView):
    queryset = Boss.objects.all()
    serializer_class = BossesSerializer
    

class BossDetailView(RetrieveAPIView):
    queryset = Boss.objects.all()
    serializer_class = BossDetailSerializer
    

class AdminstratorsListView(ListCreateAPIView):
    queryset = Adminstrator.objects.all()
    serializer_class = AdminstratorsSerializer
    

class AdminstratorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Adminstrator.objects.all()
    serializer_class = AdminstratorDetailSerializer
    

class AccountantsListView(ListCreateAPIView):
    queryset = Accountant.objects.all()
    serializer_class = AccountantsSerializer
    

class AccountantDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Accountant.objects.all()
    serializer_class = AccountantDetailSerializer
    
    
class TeacherListView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeachersSerializer
    

class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherDetailSerializer