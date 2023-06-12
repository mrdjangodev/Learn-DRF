from django.urls import path
from .views import BookApiView, BookDetailView


urlpatterns = [
    path('api/', BookApiView.as_view(), name='home'),
    path('api/<int:pk>/', BookDetailView.as_view()),
]
