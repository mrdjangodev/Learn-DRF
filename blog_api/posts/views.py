from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer
from .permissions import IsAutorOrReadOnly

# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAutorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

