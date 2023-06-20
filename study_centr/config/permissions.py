from rest_framework.permissions import BasePermission, SAFE_METHODS
from django.db.models import Q

from employee.models import (
    Adminstrator, Boss, Teacher, Accountant
    )
from students.models import Student
from marketing.models import ServiceUser


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
        else:
            return False


class BossPermissions(BasePermission):
    """Boss Can add/update/delete/see (Teacher, Accountant, Adminstrator)
        Can See StudentPayments, Interestors, Service Incomes"""
    def has_object_permission(self, request, view, obj):
        boss_exists = Boss.objects.filter(Q(user=request.user) & Q(is_active=True)).exists()
        if boss_exists and request.method in SAFE_METHODS:
            return True
        else:
            return False


class TeacherPermissions(BasePermission):
    """Teacher can update/see (Profile detail)
        Can add/see Student Attendance"""
    def has_object_permission(self, request, view, obj):
        teacher_exists = Teacher.objects.filter(Q(user=request.user) & Q(is_active=True)).exists()
        if teacher_exists and request.method in SAFE_METHODS:
            return True
        return False


class AccountantPermissions(BasePermission):
    """Accountant can Add/see (Student Payment, Extra payments, Emplee's payments, ServiceUsagePayments)
        """
    def has_permission(self, request, view):
        accountant_exists = Accountant.objects.filter(Q(user=request.user) & Q(is_active=True)).exists()
        if accountant_exists and request.method in SAFE_METHODS:
            return True
        return False
    

class StudentPermissions(BasePermission):
    """Student can see/edit profile data, 
        Can see all (schedules, groups, payments)"""
    def has_permission(self, request, view):
        student_exists = Student.objects.filter(Q(user=request.user) & Q(is_active=True)).exists()
        if student_exists and request.method in SAFE_METHODS:
            return True
        return False


class ServiceUserPermissions(BasePermission):
    """Can see All (Services, ServicePayments)
    """
    def has_permission(self, request, view):
        service_user_exists = ServiceUser.objects.filter(Q(user=request.user)).exists()
        if service_user_exists and request.method in SAFE_METHODS:
            return True
        return False