from rest_framework.generics import (ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView)
from django.shortcuts import get_object_or_404

from .models import Teacher, Accountant, Adminstrator, Boss
from .serializers import (TeachersSerializer, TeacherDetailSerializer, 
                          AccountantsSerializer, AccountantDetailSerializer,
                          BossesSerializer, BossDetailSerializer,)
from .admin_serializers import AdminstratorsSerializer, AdminstratorDetailSerializer
from .forms import TeacherForm
from main.models import CustomUser
# Create your views here.

class BossesListView(ListCreateAPIView):
    queryset = Boss.objects.prefetch_related('user')
    serializer_class = BossesSerializer
    

class BossDetailView(RetrieveAPIView): 
    queryset = Boss.objects.select_related('user')
    serializer_class = BossDetailSerializer
    

class AdminstratorsListView(ListCreateAPIView):
    queryset = Adminstrator.objects.prefetch_related('user').all()
    serializer_class = AdminstratorsSerializer
    

class AdminstratorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Adminstrator.objects.select_related('user')
    serializer_class = AdminstratorDetailSerializer
    

class AccountantsListView(ListCreateAPIView):
    queryset = Accountant.objects.prefetch_related('user')
    serializer_class = AccountantsSerializer
    

class AccountantDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Accountant.objects.select_related('user')
    #I chose select related in this view cuz I take only one related object in this view
    serializer_class = AccountantDetailSerializer
    
    
class TeacherListView(ListCreateAPIView):
    # queryset = Teacher.objects.all()
    queryset = Teacher.objects.prefetch_related('user').all() # I choose fastest queryset
    # queryset = Teacher.objects.select_related('user').all()
    """Teacher.objects.all(): This queryset fetches all the teacher objects from the database 
        without any optimization. The advantage of using this queryset is that it is simple and 
        easy to use. However, the disadvantage is that it can be slow if you have a large number 
        of teacher objects in your database, as it fetches all the data at once.

        Teacher.objects.prefetch_related('user').all(): This queryset uses prefetch_related to fetch 
        the related user objects in a separate query to avoid N+1 queries. The advantage of using this 
        queryset is that it reduces the number of database queries required to fetch related user objects,
        which can significantly improve performance. The disadvantage is that it can be memory-intensive 
        if you have a large number of related objects.

        Teacher.objects.select_related('user').all(): This queryset uses select_related to fetch 
        the related user objects in a single query instead of separate queries. The advantage of 
        using this queryset is that it is more efficient than prefetch_related, as it requires less 
        memory. The disadvantage is that it can be slower than prefetch_related if you have a large 
        number of related objects, as it fetches all the related objects at once.
    """
    serializer_class = TeachersSerializer
    

class TeacherDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.select_related('user').prefetch_related('subjects').all()
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


    