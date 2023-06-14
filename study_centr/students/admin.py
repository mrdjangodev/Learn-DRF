from django.contrib import admin

from .models import Student, StudentPayment
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_active', 'balance', 'created_at']
    list_editable = ['is_active']
admin.site.register(Student, StudentAdmin)


class StudentPaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'adminstrator', 'student', 'amount', 'created_at']
admin.site.register(StudentPayment, StudentPaymentAdmin)