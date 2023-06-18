from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView

from .models import (
    Service, ServiceUsage, ServiceUser, SocialMedia, Interestor
)
from .serializers import (
    ServicesSerializer, ServiceDetailSerializer,
    ServiceUserSerializer, ServiceUserDetailSerializer,
    ServiceUsageSerializer, ServiseUsageDetailSerializer,
    SocialMediaSerializer, SocialMediaDetailSerializer,
    InterestorsSerialer, InterestorDetailSerializer,
    )
# Create your views here.

class ServiceView(ListCreateAPIView):
    queryset = Service.objects.select_related('teacher')
    serializer_class = ServicesSerializer
    

class ServiceDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.select_related('teacher')
    serializer_class = ServiceDetailSerializer
    
    
class ServiceUserView(ListCreateAPIView):
    queryset = ServiceUser.objects.all()
    serializer_class = ServiceUserSerializer
    

class ServiceUserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ServiceUser.objects.all()
    serializer_class = ServiceUserDetailSerializer
    

class ServiceUsageView(ListCreateAPIView):
    queryset = ServiceUsage.objects.prefetch_related('service', 'user')
    serializer_class = ServiceUsageSerializer
    

class ServiceUsageDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ServiceUsage.objects.select_related('service', 'user')
    serializer_class = ServiseUsageDetailSerializer
    
    
class SocialMediaView(ListCreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    

class SocialMediaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaDetailSerializer
    
    
class InterestorsView(ListCreateAPIView):
    queryset = Interestor.objects.prefetch_related('found_us')
    serializer_class = InterestorsSerialer


class InterestorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Interestor.objects.prefetch_related('found_us')
    serializer_class = InterestorDetailSerializer