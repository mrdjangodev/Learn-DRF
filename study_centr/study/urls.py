from django.urls import path
from .views import GroupViewSet, GroupDetailView

urlpatterns = [
    path('groups/', GroupViewSet.as_view(), name='group'),
    path('group/<int:pk>/', GroupDetailView.as_view(), name="group_detail")
]
