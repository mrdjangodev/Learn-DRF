from django.contrib import admin
from .models import CustomUser, Subject, Room


# Register your models here.
# class USerAdmin(admin.ModelAdmin):
    
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']
admin.site.register(CustomUser, UserAdmin)    
    
    
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Subject, SubjectAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Room, RoomAdmin)