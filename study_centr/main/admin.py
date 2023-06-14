from django.contrib import admin
from .models import CustomUser, Subject, Room


# Register your models here.
# class USerAdmin(admin.ModelAdmin):
    
    
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Subject, SubjectAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Room, RoomAdmin)