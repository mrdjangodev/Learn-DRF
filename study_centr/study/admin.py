from django.contrib import admin

from .models import Group, Schedule
# Register your models here.
class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'teacher', 'is_active', 'name', 'price', 'created_at']
    list_editable = ['teacher', 'is_active']
admin.site.register(Group, GroupAdmin)


class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'group', 'is_active', 'start_time', 'finish_time']
admin.site.register(Schedule, ScheduleAdmin)