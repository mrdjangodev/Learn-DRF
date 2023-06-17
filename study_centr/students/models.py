from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from main.models import Subject, Room, CustomUser
from study.models import Group
from employee.models import Adminstrator
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
            result.extend(group.get_all_schedules())
        return result

    def get_all_payments(self):
        return self.studentpayment_set.all()
    
    
class StudentPayment(models.Model):
    class Meta:
        verbose_name_plural = "Students Payments"  
        ordering = ['-created_at']
    adminstrator = models.ForeignKey(Adminstrator, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f"{self.adminstrator} | {self.student}"
    
@receiver(post_save, sender=StudentPayment)
def update_student_balance(sender, instance, created, **kwargs):
    if created:
        student = instance.student
        student.balance += instance.amount
        student.save()