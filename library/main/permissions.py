from rest_framework.permissions import BasePermission, SAFE_METHODS
    
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # give access for only reading
        if request.method in SAFE_METHODS:
            return True
        # give access to edit for only book_author
        return obj.author == request.user or request.user.is_superuser  

