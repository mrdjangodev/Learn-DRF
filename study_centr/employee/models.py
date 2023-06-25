from django.db import models

from main.models import CustomUser, Subject
from .variables import employees_permissions
# from study.models import Schedule
# Create your models here.

class Boss(models.Model):
    
    class Meta:
        verbose_name_plural = "Bosses"
        ordering = ['-created_at']    
        permissions = employees_permissions['boss']
        
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user}"
    
    def calculate_kpi(self):
        pass
    
    
class Adminstrator(models.Model):
    class Meta:
        verbose_name_plural = 'Admintrators'
        ordering = ['-created_at']
        permissions = employees_permissions['adminstrator']
        
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user}"
    
    def calculate_kpi(self):
        pass
    
    
class Accountant(models.Model):
    class Meta:
        verbose_name_plural = 'Accountants'
        ordering = ['-created_at']
        permissions = employees_permissions['accountant']
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user}"
    
    def calculate_kpi(self):
        pass
    
class Teacher(models.Model):
    class Meta:
        verbose_name_plural = 'Teachers'
        ordering = ['-created_at']
        permissions = employees_permissions['teacher']
        
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    subjects = models.ManyToManyField(Subject)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self) -> str:
        return f"{self.user}"
    
    def calculate_kpi(self):
        pass
    
    
    def get_all_schedules(self):
        schedules = []
        for group in self.get_all_groups():
            schedules.extend(group.schedule_set.all().select_related('group', 'room'))
        return schedules
    
    def get_all_groups(self):
        return self.group_set.select_related('teacher').all()
        # pass
        

# signals here
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Permission



@receiver(post_save, sender=Boss)
@receiver(post_save, sender=Teacher)
@receiver(post_save, sender=Adminstrator)
def change_user_staff_status(sender, instance, created, **kwargs):
    """Grant access to Django's admin dashboard for new employees."""
    if created and hasattr(instance, 'user'):
        user = instance.user
        user.is_staff = True
        model_name = instance.__class__.__name__.lower()
        permissions = employees_permissions.get(model_name)
        permission_ids = []
        for codename, name in permissions:
            permission = Permission.objects.filter(name__icontains=name).exclude(content_type__app_label='auth')
            if len(permission) > 1:
                for pr in permission:
                    permission_ids.append(pr.id)
            elif len(permission) == 1:
                permission_ids.append(permission[0].id)
        print("Perm IDs: ", permission_ids)
        auth_permission_ids = Permission.objects.filter(content_type__app_label='auth').values_list('id', flat=True)
        user.user_permissions.add(*permission_ids)
        user.save()
        user_perms_ids = user.user_permissions.all().values_list('id', flat=True) #user permission after saving
        conflict_ids = list(set(permission_ids) - set(user_perms_ids))
        print(f"Conflict ids: {conflict_ids}")
        user.user_permissions.remove(*auth_permission_ids)
        if permission_ids != []:
            user.user_permissions.add(*conflict_ids)
            user.save()
        final_user_perms_ids = [perm_id for perm_id in user.user_permissions.all().values_list('id', flat=True)]
        
        print(f"Difference beetween: before/after conflict\n{list(set(final_user_perms_ids) - set(user_perms_ids))}")
        # auth_permission_ids = Permission.objects.filter(content_type__app_label='auth').values_list('id', flat=True)
        
        # print(f"SocialMediaPermissions: {social_media_perms}\n{10*'*'}\nall_perms_ids: {permission_ids}")
   