from django.db import models

from main.models import CustomUser, Subject
# from study.models import Schedule
# Create your models here.

class Boss(models.Model):
    
    class Meta:
        verbose_name_plural = "Bosses"
        ordering = ['-created_at']    
        
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

from .variables import employees_permissions

@receiver(post_save, sender=Boss)
@receiver(post_save, sender=Teacher)
@receiver(post_save, sender=Adminstrator)
def change_user_staff_status(sender, instance, created, **kwargs):
    """Grant access to Django's admin dashboard for new employees."""
    if created and hasattr(instance, 'user'):
        user = instance.user
        user.is_staff = True
        model_name = instance.__class__.__name__.lower()
        # print(f"Model name: {model_name}")
        permissions = employees_permissions.get(model_name)
        # print(f"Perms: {permissions}")
        # print(f"All CustomUser permissions: {Permission.objects.all()}")
        permission_ids = []
        for codename, name in permissions:
            # print(name)
            permission = tuple(set(Permission.objects.filter(name=name)))
            # print(f"Perm: ",permission)
            if len(permission) > 1:
                for pr in permission:
                    permission_ids.append(pr.id)
                else:
                    permission_ids.append(permission[0].id)
            # permission = Permission.objects.filter(name=name)
        # print(permission_ids)
        
            
        user.user_permissions.add(*permission_ids)
        user.save()
        
        print(f"User: {user} | is_staff: {user.is_staff}\nPermissions: {user.user_permissions}")