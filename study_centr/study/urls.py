from django.urls import path
from .views import GroupViewSet, GroupDetailView, ScheduleView, ScheduleDetailView

urlpatterns = [
    path('groups/', GroupViewSet.as_view(), name='groups'),
    path('group/<int:pk>/', GroupDetailView.as_view(), name="group_detail"),
    
    path('schedules/', ScheduleView.as_view(), name='schedules'),
    path('schedule/<int:pk>/', ScheduleDetailView.as_view(), name="schedule_detail"),
]
