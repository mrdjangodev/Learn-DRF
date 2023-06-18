from django.urls import path

from .views import (UserViewSet, UserDetailViewSet, RoomViewSet, 
                    RoomDetailViewSet, SubjectViewSet, SubjectDetailViewSet)

urlpatterns = [
    path('users/', UserViewSet.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailViewSet.as_view(), name='user_detail'),
    
    path('rooms/', RoomViewSet.as_view(), name='rooms'),
    path('rooms/<int:pk>/', RoomDetailViewSet.as_view(), name='room_detail'),
    
    path('subjects/', SubjectViewSet.as_view(), name='subjects'),
    path('subject/<int:pk>/', SubjectDetailViewSet.as_view(), name='subject_detail'),
]