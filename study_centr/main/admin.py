from django.contrib import admin
from .models import CustomUser, Subject, Room
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Register your models here.
# class USerAdmin(admin.ModelAdmin):

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2'),
        }),
    )
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ('email', 'username', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'username', 'first_name', 'last_name')
    ordering = ('email',)
    
admin.site.register(CustomUser, CustomUserAdmin)
    
    
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Subject, SubjectAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
admin.site.register(Room, RoomAdmin)