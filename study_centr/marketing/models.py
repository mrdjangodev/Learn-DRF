from django.db import models
from django.core.exceptions import ValidationError
# from time import datetime
from datetime import timedelta, datetime


from main.models import CustomUser
from employee.models import Teacher

class Service(models.Model):
    class Meta:
        verbose_name_plural = 'Services'
        ordering = ['-created_at']
    name = models.CharField(max_length=150, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    is_active = models.BooleanField(default=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name + '|' + str(self.price)+'UZS'
    
    def get_all_usages(self):
        return self.serviceusage_set.prefetch_related('user', 'service')
    
    def get_all_done_usages(self):
        """
        In general, it is better to apply the filter method 
        before the prefetch_related method because it reduces 
        the amount of data that needs to be retrieved from 
        the database. The filter method applies a filter on the 
        ServiceUsage objects before they are retrieved from 
        the database, which means that only the relevant ServiceUsage 
        objects will be retrieved. On the other hand,   
        the prefetch_related method retrieves all related User 
        and Service objects for all retrieved ServiceUsage objects, 
        which can be a large amount of data if there are many ServiceUsage objects."""
        return self.serviceusage_set.filter(is_done=True).prefetch_related('user', 'service')
    
    def get_daily_usages(self):
        today = datetime.now().date()
        return self.serviceusage_set.filter(created_at__date=today).select_related('user', 'service')

    def get_weekly_usages(self):
        today = datetime.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        return self.serviceusage_set.filter(created_at__range=(start_of_week, end_of_week)).select_related('user', 'service')

    def get_monthly_usages(self):
        current_month = datetime.now().month
        return self.serviceusage_set.filter(created_at__month=current_month).select_related('user', 'service')
    
    def get_total_income(self):
        return self.serviceusage_set.filter(payment_done=True).aggregate(total_income=models.Sum('service__price'))['total_income'] or 0


class SocialMedia(models.Model):
    class Meta:
        verbose_name_plural = 'Social Medias'
        ordering = ['-created_at']
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField()
    followers = models.PositiveBigIntegerField(default=0)
    effect = models.DecimalField(max_digits=4, decimal_places=2, default=0.0) #that is precentage of visitors by this social media to centr
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
    
    def get_all_interestors(self):
        return self.interestor_set.all().prefetch_related('found_us')

    def get_this_month_interestors(self):
        current_month = datetime.now().month
        return self.interestor_set.filter(created_at__month=current_month).prefetch_related('found_us')

    def get_this_week_interestors(self):
        current_week = datetime.now().isocalendar()[1]
        return self.interestor_set.filter(created_at__week=current_week).select_related('found_us')

    def get_daily_interestors(self):
        today = datetime.now().date()
        return self.interestor_set.filter(created_at__date=today).select_related('found_us')
    

class Interestor(models.Model):
    class Meta:
        verbose_name_plural = 'Interestors'
        ordering = ['-created_at']
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    found_us = models.ForeignKey(SocialMedia, on_delete=models.CASCADE, null=True, default=None)
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
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    payment_done = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.user} | {self.service}"
    
    
    
#ServicePayment section start 
def validate_service_payment(value):
    if value.service_usage.payment_done == True:
        raise ValidationError(f"Service Usage's Payment is already done")
    
    elif value.service_user != value.service_usage.user:
        raise ValidationError(f"service_user should be the same with ({value.service_usage.user})")
    
    elif value.service != value.service_usage.service:
        raise ValidationError(f"service should be the same with ({value.service_usage.service})")
    
    elif value.service.price > value.amount:
        raise ValidationError(f'Amount should be Greater than or equal to ({value.service.price})')
    
    
class ServicePayment(models.Model):
    class Meta:
        verbose_name_plural = 'Service Payments'
        ordering = ['-created_at']
    service_usage = models.ForeignKey(ServiceUsage, on_delete=models.CASCADE)
    service_user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.service_usage }"
    
    def clean(self):
        super().clean()
        validate_service_payment(self)
        
        
# signals here
from django.dispatch import receiver
from django.db.models.signals import post_save

# @receiver(post_save, sender=ServiceUsage)
# def update_service_user_status(sender, instance, created, **kwargs):
#     if created:
#         user = instance.user
#         usage_count = user.get_all_usages().filter(payment_done=True).count()
#         if usage_count >= 1:
#             user.status = 'normal'
#         elif usage_count > 5:
#             user.status = 'loyal'
#         user.save()
        
@receiver(post_save, sender=ServicePayment)
def update_service_usage_payment_done(sender, instance, created, **kwargs):
    if created:
        user = instance.service_user
        usage = instance.service_usage
        if usage.payment_done == False:
            usage.payment_noe = True
            usage.save()
        usage_count = user.get_all_usages().filter(payment_done=True).count()
        if usage_count >= 1:
            user.status = 'normal'
        elif usage_count > 5:
            user.status = 'loyal'
        user.save()