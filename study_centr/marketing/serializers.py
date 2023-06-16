from rest_framework import serializers

from .models import (
    Service, ServiceUsage, ServiceUser, SocialMedia, Interestor
)

# serializers section 

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'