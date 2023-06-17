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
    
    def __str__(self):
        return self.name
    
    
    def get_debtor_students(self):
        return self.students.objects_set.perfetch_related('group').all().filter(balance__lt=0)
        
    def get_all_students(self):
        return self.students.objects_set.select_related('user').perfetch_related('group').all()
        
    def get_all_active_students(self):
        return self.get_all_students.filter(is_active=True)
    
    def get_all_schedules(self):
        return self.schedule_set.select_related('group', 'room')
    
    
class Schedule(models.Model):
    class Meta:
        verbose_name_plural = 'Schedules'
        ordering = ['-start_time']
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"room: {self.room} | group: {self.group} | is_active: {self.is_active}"