from django.urls import path
from  .views import (BossesListView, BossDetailView, 
                     AdminstratorsListView, AdminstratorDetailView,
                     AccountantsListView, AccountantDetailView,
                     TeacherListView, TeacherDetailView, update_teacher)


urlpatterns = [
    path('bosses/', BossesListView.as_view(), name='bosses'),
    path('boss/<int:pk>/', BossDetailView.as_view(), name='boss_detail'),
    
    path('adminstrators/', AdminstratorsListView.as_view(), name='adminstrators'),
    path('adminstrator/<int:pk>/', AdminstratorDetailView.as_view(), name='adminstrator_detail'),
    
    path('accountants/', AccountantsListView.as_view(), name='accountants'),
    path('accountant/<int:pk>/', AccountantDetailView.as_view(), name='accountant_detail'),
    
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('teacher/<int:pk>/', TeacherDetailView.as_view(), name='teachers_detail'),
    
]