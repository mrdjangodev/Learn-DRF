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
    

class ServiceDetailSerializer(serializers.ModelSerializer):
    total_income = serializers.SerializerMethodField("get_total_income", read_only=True)
    all_users = serializers.SerializerMethodField("get_all_users", read_only=True)
    all_usages = serializers.SerializerMethodField("get_all_usages", read_only=True)
    all_done_usages = serializers.SerializerMethodField("get_all_done_usages", read_only=True)

    # total_users = serializers.SerializerMethodField('get_number_of_users', read_only=True)
    # total_usages = serializers.SerializerMethodField("get_number_of_usages", read_only=True)
    # total_done_usages = serializers.SerializerMethodField("get_number_of_done_usages", read_only=True)
    
    total_users = all_users.count()
    total_usages = all_usages.count()
    total_done_usages = all_done_usages.count()
    
    daily_usages = serializers.SerializerMethodField("get_daily_usages", read_only=True)
    weekly_usages = serializers.SerializerMethodField("get_weekly_usages", read_only=True)
    montly_usages = serializers.SerializerMethodField("get_montly_usages", read_only=True).count()

    total_daily_usages = daily_usages.count()
    total_weekly_usages = weekly_usages.count()
    total_montly_usages = montly_usages.count()
    
    class Meta:
        model = Service
        fields = (
            'id', 'name', 'is_active', 'description',
            'created_at', 'total_users', 'total_usages', 
            'total_done_usages', 'total_income', 
            'total_daily_usages', 'total_weekly_usages',
            'total_montly_usages', 'all_users', 'all_usages', 
            'all_done_usages', 'daily_usages', 'weekly_usages',
            'montly_usages'
            )
        
    # def get_number_of_users(self, obj):
    #     return obj.get_all_users().count()
    
    # def get_number_of_usages(self, obj):
    #     return obj.get_all_usages().count(),
    
    # def get_number_of_done_usages(self, obj):
    #     return obj.get_all_done_usages().count()
    
    def get_total_income(self, obj):
        return obj.get_total_income()
    
    def get_all_users(self, obj):
        return obj.get_all_users()
    
    def get_all_usages(self, obj):
        return obj.get_all_usages()
    
    def get_all_done_usages(self, obj):
        return obj.get_all_done_usages()
    
    def get_daily_usages(self, obj):
        return obj.get_all_daily_usages()
    
    def get_weekly_usages(self, obj):
        return obj.get_all_weekly_usages()
    
    def get_monthly_usages(self, obj):
        return obj.get_all_monthly_usages()