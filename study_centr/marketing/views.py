from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from .models import (
    Service, ServiceUsage, ServiceUser, SocialMedia, Interestor
)
from .serializers import (
    ServicesSerializer, ServiceDetailSerializer,
    )
# Create your views here.

class ServiceSerializer(ListCreateAPIView):
    model = Service.objects.select_related('teacher')
    serializer_class = ServicesSerializer
    

class ServiceDetailSerializer(RetrieveUpdateDestroyAPIView):
    model = Service.select_related('teacher')
    serializer_class = ServiceDetailSerializer
    