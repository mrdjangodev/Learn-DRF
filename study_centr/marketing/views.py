from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from .models import (
    Service, ServiceUsage, ServiceUser, SocialMedia, Interestor
)
from .serializers import (
    ServicesSerializer, ServiceDetailSerializer,
    ServiceUserSerializer, ServiceUserDetailSerializer,
    )
# Create your views here.

class ServiceView(ListCreateAPIView):
    queryset = Service.objects.select_related('teacher')
    serializer_class = ServicesSerializer
    

class ServiceDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.select_related('teacher')
    serializer_class = ServiceDetailSerializer
    
    
class ServiceUserView(ListCreateAPIView):
    queryset = ServiceUser.objects.prefetch_related('get_all_usages_set')
    serializer_class = ServiceUserSerializer
    

class ServiceUserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ServiceUser.objects.prefetch_related('get_all_usages_set')
    serializer_class = ServiceDetailSerializer
    
