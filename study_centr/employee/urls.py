from django.urls import path
from  .views import (BossesListView, BossDetailView, 
                     AdminstratorsListView, AdminstratorDetailView,
                     AccountantsListView, AccountantDetailView,
                     TeacherListView, TeacherDetailView, update_teacher)


urlpatterns = [
    path('bosses/', BossesListView.as_view()),
    path('boss/<int:pk>/', BossDetailView.as_view()),
    
    path('adminstrators/', AdminstratorsListView.as_view()),
    path('adminstrator/<int:pk>/', AdminstratorDetailView.as_view()),
    
    path('accountants/', AccountantsListView.as_view()),
    path('accountant/<int:pk>/', AccountantDetailView.as_view()),
    
    path('teachers/', TeacherListView.as_view()),
    # path('teachers/<int:pk>/', update_teacher),
    path('teacher/<int:pk>/', TeacherDetailView.as_view()),
    
]