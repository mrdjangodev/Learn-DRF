from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from .models import (
    Service, ServiceUsage, ServiceUser, SocialMedia, Interestor
)
from .serializers import (
    ServicesSerializer, ServiceDetailSerializer,
    )
# Create your views here.

class ServiceView(ListCreateAPIView):
    queryset = Service.objects.select_related('teacher')
    serializer_class = ServicesSerializer
    

class ServiceDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.select_related('teacher')
    serializer_class = ServiceDetailSerializer
    