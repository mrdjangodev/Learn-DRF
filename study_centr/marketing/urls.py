from django.urls import path

from .views import (
    ServiceView, ServiceDetailView, 
    ServiceUserView, ServiceUserDetailView,
)

urlpatterns = [
    path('services/', ServiceView.as_view(), name='services'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    
    path('services/users/', ServiceUserView.as_view(), name='service_users'),
    path('services/user/<int:pk>/', ServiceUserDetailView.as_view(), name='service_user_detail'),
    
    
]