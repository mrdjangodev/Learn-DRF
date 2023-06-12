from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PostList, PostDetail, UserList, UserDetail, PostViewSet, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='userds')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls
# [    
#     path('users/', UserList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
    
#     path("", PostList.as_view()),
#     path("<int:pk>/", PostDetail.as_view()),
# ]