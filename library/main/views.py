from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly

class BookApiView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class BookDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
    queryset = Book.objects.all()
    serializer_class = BookSerializer