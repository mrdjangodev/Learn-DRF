from rest_framework.permissions import BasePermission, SAFE_METHODS
from employee.models import Adminstrator, Boss
from django.db.models import Q


class AdminstratorPermissions(BasePermission):
    """Adminstrators can Add/update/delete/view (Teacher, Student, Subject, Group, Room, Schedule, SocialMedia)
        Can See only Debtor Students
        Can Add/See StudentPayment
        Can Add/Update/see Service, ServiceUsage"""
    def has_object_permission(self, request, view, obj):
        admin_exists = Adminstrator.objects.filter(Q(user=request.user) & Q(is_active=True)).exists()
        # give access for only reading
        if request.method in SAFE_METHODS and admin_exists:
            return True
 

class BossPermissions(BasePermission):
    """Boss Can add/update/delete/see (Teacher, Accountant, Adminstrator)
        Can See StudentPayments, Interestors, Service Incomes"""
    def has_object_permission(self, request, view, obj):
        boss_exists = Boss.objects.filter(Q(user=request.user) & Q(is_active=True)).exists()
        if boss_exists and request.method in SAFE_METHODS:
            return True
    

