from rest_framework.generics import (ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView)
from django.shortcuts import get_object_or_404

from .models import Teacher, Accountant, Adminstrator, Boss
from .serializers import (TeachersSerializer, TeacherDetailSerializer, 
                          AccountantsSerializer, AccountantDetailSerializer,
                          AdminstratorsSerializer, AdminstratorDetailSerializer, 
                          BossesSerializer, BossDetailSerializer,)
from .forms import TeacherForm
from main.models import CustomUser
# Create your views here.

class BossesListView(ListCreateAPIView):
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
    
    # def perform_update(self, serializer):
    #     print("soMethingj")
    #     serializer.save(user_data=self.request.data.get('user_data', {}))
        
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.serializers.json import DjangoJSONEncoder
import json

@api_view(['GET', 'PUT'])
def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, id=pk)
    if request.method == 'PUT':
        form = TeacherForm(request.data, instance=teacher)
        if form.is_valid():
            form.save()
            serializer = TeacherDetailSerializer(instance=teacher)
            return Response(serializer.data)
        else:
            return Response(form.errors, status=400)
    else:
        serializer = TeacherDetailSerializer(instance=teacher)
        form = TeacherForm(instance=teacher)

        context = {
            'serializer': serializer.data,
            'form': json.dumps(form, cls=DjangoJSONEncoder),
        }

        return Response(context)
    # if request.method == 'PUT':
    #     form = TeacherForm(request.data, instance=teacher)
    #     if form.is_valid():
    #         form.save()
    #         serializer = TeacherDetailSerializer(instance=teacher)
    #         return Response(serializer.data)
    #     else:
    #         return Response(form.errors, status=400)
    # else:
    #     serializer = TeacherDetailSerializer(instance=teacher)
    #     form = TeacherForm(instance=teacher)

    #     context = {
    #         'serializer': serializer,
    #         'form': form
    #     }

    #     return Response(context)


    