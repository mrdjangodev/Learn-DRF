from django.urls import path

from .views import (
    ServiceView, ServiceDetailView, 
    ServiceUserView, ServiceUserDetailView,
    ServiceUsageView, ServiceUsageDetailView,
    SocialMediaView, SocialMediaDetailView,
)

urlpatterns = [
    path('services/', ServiceView.as_view(), name='services'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    
    path('services/users/', ServiceUserView.as_view(), name='service_users'),
    path('services/user/<int:pk>/', ServiceUserDetailView.as_view(), name='service_user_detail'),
    
    path('services/usages/', ServiceUsageView.as_view(), name="service_usages"),
    path('service/usage/<int:pk>/', ServiceUsageDetailView  .as_view(), name="service_usage_detail"),
    
    path('social-medias/', SocialMediaView.as_view(), name="social_medias"),
    path('social-media/<int:pk>/', SocialMediaDetailView.as_view(), name='social_media_detail'),
]