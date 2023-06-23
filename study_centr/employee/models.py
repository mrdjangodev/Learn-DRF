from django.db import models

from main.models import CustomUser, Subject
# from study.models import Schedule
# Create your models here.

class Boss(models.Model):
    
    class Meta:
        verbose_name_plural = "Bosses"
        ordering = ['-created_at']    
        permissions = (
            ('can_view_boss', 'Can view boss'),
            ('can_add_boss', 'Can add boss'),
            ('can_change_boss', 'Can change boss'),
            ('can_delete_boss', 'Can delete boss'),
            
            ('view_teacher', "Can view teacher"),
            ('add_teacher', 'Can add teacher'),
            ('change_teacher', 'Can change teacher'),
            ('delete_teacher', 'Can delete teacher'),
            
            ('view_adminstrator', "Can view adminstrator"),
            ('add_adminstrator', 'Can add adminstrator'),
            ('change_adminstrator', 'Can change adminstrator'),
            ('delete_adminstrator', 'Can delete adminstrator'),
            
            ('view_accountant', "Can view accountant"),
            ('add_accountant', 'Can add accountant'),
            ('change_accountant', 'Can change accountant'),
            ('delete_accountant', 'Can delete accountant'),
            
            ('view_services', 'Can view services'),
            ('view_subjects', 'Can view subjects'),
            ('view_groups', 'Can view groups'),
        )
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
        permissions = (
            ('can_view_teacher', "Can view teacher"),
            ('can_add_teacher', 'Can add teacher'),
            ('can_change_teacher', 'Can change teacher'),

            ('can_view_student', "Can view student"),
            ('can_add_student', 'Can add student'),
            ('can_change_student', 'Can change student'),
            
            ('can_view_studentpayment', "Can view studentpayment"),
            ('can_add_studentpayment', 'Can add studentpayment'),
            
            ('can_view_room', "Can view room"),
            ('can_add_room', 'Can add room'),
            ('can_change_room', 'Can change room'),
            
            ('can_view_subject', "Can view subject"),
            ('can_add_subject', 'Can add subject'),
            ('can_change_subject', 'Can change subject'),
            
            ('can_view_group', "Can view group"),
            ('can_add_group', 'Can add group'),
            ('can_change_group', 'Can change group'),
            
            ('can_view_socialmedia', "Can view socialmedia"),
            ('can_add_socialmedia', 'Can add socialmedia'),
            ('can_change_socialmedia', 'Can change socialmedia'),
            
            ('can_view_service', "Can view service"),
            ('can_add_service', 'Can add service'),
            ('can_change_service', 'Can change service'),
            
            ('can_view_serviceuser', "Can view serviceuser"),
            ('can_add_serviceuser', 'Can add serviceuser'),
            
            ('can_view_serviceusage', "Can view serviceusage"),
            ('can_add_serviceusage', 'Can add serviceusage'),
            ('can_change_serviceusage', 'Can change serviceusage'),
            
            ('can_view_schedule', "Can view schedule"),
            ('can_add_schedule', 'Can add schedule'),
            ('can_change_schedule', 'Can change schedule'),
            ('can_delete_schedule', 'Can delete schedule'),
            
            ('can_view_servicepayment', "Can view servicepayment"),
            ('can_add_servicepayment', 'Can add servicepayment'),
            
            ('can_view_interestor', "Can view interestor"),          
        )
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
        # permissions = (
        #     ('can_view_attandance', "Can view attandance"),
        #     ('can_add_attandance', 'Can add attandance'),
        #     ('can_change_attandance', 'Can change attandance'),
        #     )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
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