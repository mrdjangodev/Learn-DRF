from django.db import models


from main.models import CustomUser, Subject
# Create your models here.

class Boss(models.Model):
    
    class Meta:
        verbose_name_plural = "Bosses"
        ordering = ['-created_at']    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    subjects = models.ManyToManyField(Subject)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def __str__(self) -> str:
        return f"{self.user}"
    
    def get_all_groups(self):
        return self.group.objects.set_all()
    
    def get_all_schedules(self):
        return self.schedule.object.all()