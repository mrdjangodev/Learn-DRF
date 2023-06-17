from django.urls import path


from .views import (
    StudentsListView, StudentsDetailView, StudentsPaymentsView, StudentsPaymentDetailView
)
urlpatterns = [
    path('', StudentsListView.as_view(), name='students_list'),
    path('<int:pk>/', StudentsDetailView.as_view(), name='student_detail'),
    
    path('payments/', StudentsPaymentsView.as_view(), name='payments'),
    path('payment/<int:pk>/', StudentsPaymentDetailView.as_view(), name='payment_detail'),
]
