from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from .serializers import StudentSerializer, StudentDetailSerializer, StudentPaymentSerializer, StudentPaymentDetailSerializer
from .models import StudentPayment, Student
# Create your views here.

class StudentsListView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

class StudentsDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    

class StudentsPaymentsView(ListCreateAPIView):
    queryset = StudentPayment.objects.all()
    serializer_class = StudentPaymentSerializer
    

class StudentsPaymentDetailView(RetrieveAPIView):
    queryset = StudentPayment.objects.all()
    serializer_class = StudentPaymentDetailSerializer