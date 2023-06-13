from django.db import models


from main.models import Room, Subject
from employee.models import Teacher
# Create your models here.

class Group(models.Model):
    class Meta:
        verbose_name_plural = 'Groups'
        ordering = ['-created_at']
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    
    def get_debtor_students(self):
        return self.students.objects.set_all().filter(balance__lt=0)
        
    def get_all_students(self):
        return self.students.objects.set_all()
        
    def get_all_active_students(self):
        return self.students.objects.set_all().filter(is_active=True)
    
    def get_all_schedules(self):
        return self.schedule.objects.set_all()