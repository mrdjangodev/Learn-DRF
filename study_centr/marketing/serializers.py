from rest_framework import serializers

from .models import (
    Service, ServiceUsage, ServiceUser, SocialMedia, Interestor
)

# serializers section 

class ServicesSerializer(serializers.ModelSerializer):
    
    total_users = serializers.SerializerMethodField('get_number_of_users', read_only=True)
    total_usages = serializers.SerializerMethodField("get_number_of_usages", read_only=True)
    total_done_usages = serializers.SerializerMethodField("get_number_of_done_usages", read_only=True)
    total_income = serializers.SerializerMethodField("get_total_income", read_only=True)
    
    class Meta:
        model = Service
        fields = ('id', 'name', 'is_active', 'description', \
            'created_at', 'total_users', 'total_usages', 'total_done_usages',\
            'total_income')
        
    def get_number_of_users(self, obj):
        return obj.get_all_users().count()
    
    def get_number_of_usages(self, obj):
        return obj.get_all_usages().count(),
    
    def get_number_of_done_usages(self, obj):
        return obj.get_all_done_usages().count()
    
    def get_total_income(self, obj):
        return obj.get_total_income()
    