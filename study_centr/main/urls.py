from django.urls import path

from .views import (UserViewSet, UserDetailViewSet, RoomViewSet, 
                    RoomDetailViewSet, SubjectViewSet, SubjectDetailViewSet)

urlpatterns = [
    path('users/', UserViewSet.as_view()),
    path('users/<int:pk>/', UserDetailViewSet.as_view()),
    
    path('rooms/', RoomViewSet.as_view()),
    path('rooms/<int:pk>/', RoomDetailViewSet.as_view()),
    
    path('subjects/', SubjectViewSet.as_view()),
    path('subject/<int:pk>/', SubjectDetailViewSet.as_view()),
]