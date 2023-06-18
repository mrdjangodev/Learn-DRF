from django.urls import path

from .views import (
    ServiceView, ServiceDetailView
)

urlpatterns = [
    path('services/', ServiceView.as_view(), name='services'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    
    
]