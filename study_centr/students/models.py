from django.db import models

from main.models import Subject, Room, CustomUser
from study.models import Group
# Create your models here.

class Student(models.Model):
    class Meta:
        verbose_name_plural = 'Students'
        ordering = ['-created_at']
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    group = models.ManyToManyField(Group)
    is_active = models.BooleanField(default=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user}"
    
    def get_all_schedules(self):
        result = []
        for group in self.group.all().filter(is_active=True):
            result.append(*tuple(group.get_all_schedules()))
        return result
    
    
    