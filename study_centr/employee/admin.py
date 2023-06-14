from django.contrib import admin

from .models import Boss, Adminstrator, Accountant, Teacher

# Register your models here.
class BossAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_active', 'salary', 'created_at']
    list_editable = ['is_active', 'salary']
admin.site.register(Boss, BossAdmin)


class AdminstratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_active', 'salary', 'created_at']
    list_editable = ['is_active', 'salary']
admin.site.register(Adminstrator, AdminstratorAdmin)


class AccountantAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_active', 'salary', 'created_at']
    list_editable = ['is_active', 'salary']
admin.site.register(Accountant, AccountantAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'is_active', 'salary', 'created_at']
    list_editable = ['is_active', 'salary']
admin.site.register(Teacher, TeacherAdmin)