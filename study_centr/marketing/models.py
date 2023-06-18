from django.db import models


from main.models import CustomUser
from employee.models import Teacher
# Create your models here.
from time import timezone

class Service(models.Model):
    class Meta:
        verbose_name_plural = 'Services'
        ordering = ['-created_at']
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_active = models.BooleanField(default=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name + '|' + str(self.price)+'UZS'
    
    def get_total_income(self):
        return self.price * self.serviceuser.set_all().count()


class SocialMedia(models.Model):
    class Meta:
        verbose_name_plural = 'Social Medias'
        ordering = ['-created_at']
    name = models.CharField(max_length=30)
    description = models.TextField()
    followers = models.PositiveBigIntegerField(default=0)
    effec = models.DecimalField(max_digits=3, decimal_places=2, default=0.0) #that is precentage of visitors by this social media to centr
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    def get_all_interestors(self):
        return self.interestor_set.all().select_related('found_us')

    def get_this_month_interestors(self):
        current_month = timezone.now().month
        return self.interestor_set.filter(created_at__month=current_month).select_related('found_us')

    def get_this_week_interestors(self):
        current_week = timezone.now().isocalendar()[1]
        return self.interestor_set.filter(created_at__week=current_week).select_related('found_us')

    def get_daily_interestors(self):
        today = timezone.now().date()
        return self.interestor_set.filter(created_at__date=today).select_related('found_us')
    

class Interestor(models.Model):
    class Meta:
        verbose_name_plural = 'Interestors'
        ordering = ['-created_at']
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    found_us = models.ForeignKey(SocialMedia, on_delete=models.DO_NOTHING, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.first_name} | {self.last_name}"
    
    
class ServiceUser(models.Model):
    class Meta:
        verbose_name_plural = 'Service Users'
        ordering = ['full_name']
    full_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='service_users/', blank=True)
    STATUS_CHOICE = (
        ('new', "New User"),#this is for new service users
        ('normal', 'Normal User'),#this is for usage count between(1: 5)
        ('loyal', "Loyal User"),# this is for usage count > 5
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='new')
    
    def __str__(self) -> str:
        return self.full_name
    
    def get_all_usages(self):
        return self.serviceusage_set.select_related('user', 'service').all()
    

class ServiceUsage(models.Model):
    class Meta:
        verbose_name_plural = 'Service Usages'
        ordering = ['-created_at']
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    is_done = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user} | {self.service}"
    


# signals here
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=ServiceUsage)
def update_service_user_status(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        usage_count = user.get_all_usages().filter(is_done=True).count()
        if usage_count >= 1:
            user.status = 'normal'
        elif usage_count > 5:
            user.status = 'loyal'
        user.save()