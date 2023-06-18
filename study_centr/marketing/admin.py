from django.contrib import admin

from .models import (
    ServicePayment, Service, ServiceUsage, ServiceUser, SocialMedia, Interestor
)
# Register your models here.

admin.site.register(Service)
admin.site.register(ServicePayment)
admin.site.register(ServiceUsage)
admin.site.register(ServiceUser)
admin.site.register(SocialMedia)
admin.site.register(Interestor)