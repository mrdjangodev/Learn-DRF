from rest_framework import serializers

from .models import (
    Service, ServiceUsage, ServiceUser, SocialMedia, Interestor
)

# serializers section 

class ServicesSerializer(serializers.ModelSerializer):
    
    total_usages = serializers.SerializerMethodField("get_number_of_usages", read_only=True)
    total_done_usages = serializers.SerializerMethodField("get_number_of_done_usages", read_only=True)
    total_income = serializers.SerializerMethodField("get_total_income", read_only=True)
    
    class Meta:
        model = Service
        fields = (
            'id', 'name', 'teacher', 'is_active', 'price', 
            'description', 'created_at', 'total_usages', 
            'total_done_usages', 'total_income')   
    
    def get_number_of_usages(self, obj):
        return obj.get_all_usages().count(),
    
    def get_number_of_done_usages(self, obj):
        return obj.get_all_done_usages().count()
    
    def get_total_income(self, obj):
        return obj.get_total_income()
    

class ServiceDetailSerializer(serializers.ModelSerializer):
    total_income = serializers.SerializerMethodField("get_total_income", read_only=True)
    all_usages = serializers.SerializerMethodField("get_all_usages", read_only=True)
    all_done_usages = serializers.SerializerMethodField("get_all_done_usages", read_only=True)

    total_usages = serializers.SerializerMethodField("get_number_of_usages", read_only=True)
    total_done_usages = serializers.SerializerMethodField("get_number_of_done_usages", read_only=True)
    
    daily_usages = serializers.SerializerMethodField("get_daily_usages", read_only=True)
    weekly_usages = serializers.SerializerMethodField("get_weekly_usages", read_only=True)
    montly_usages = serializers.SerializerMethodField("get_monthly_usages", read_only=True)

    total_daily_usages = serializers.SerializerMethodField("get_total_daily_usages", read_only=True)
    total_weekly_usages = serializers.SerializerMethodField("get_total_weekly_usages", read_only=True)
    total_monthly_usages = serializers.SerializerMethodField("get_total_monthly_usages", read_only=True)
    
    class Meta:
        model = Service
        fields = (
            'id', 'name', 'is_active', 'teacher', 'price', 'description',
            'created_at', 'total_usages', 
            'total_done_usages', 'total_income', 
            'total_daily_usages', 'total_weekly_usages',
            'total_monthly_usages', 'all_usages',
            'all_done_usages', 'daily_usages', 'weekly_usages',
            'montly_usages'
            )
        

    def get_number_of_usages(self, obj):
        return self.get_all_usages(obj).count()
    
    def get_number_of_done_usages(self, obj):
        return self.get_all_done_usages(obj).count()
    
    def get_total_daily_usages(self, obj):
        return obj.get_daily_usages().count()
    
    def get_total_weekly_usages(self, obj):
        return self.get_weekly_usages(obj).count()
    
    def get_total_monthly_usages(self, obj):
        return self.get_monthly_usages(obj).count()
    
    def get_total_income(self, obj):
        return obj.get_total_income()
    
    def get_all_usages(self, obj):
        return obj.get_all_usages()
    
    def get_all_done_usages(self, obj):
        return obj.get_all_done_usages()
    
    def get_daily_usages(self, obj):
        return obj.get_daily_usages()
    
    def get_weekly_usages(self, obj):
        return obj.get_weekly_usages()
    
    def get_monthly_usages(self, obj):
        return obj.get_monthly_usages()
    
  
class ServiceUserSerializer(serializers.ModelSerializer):
    total_usages = serializers.SerializerMethodField('get_number_of_usages', read_only=True)
    class Meta:
        model = ServiceUser
        fields = ('id', 'full_name', 'phone', 'image', 'status', 'total_usages')
    
    def get_number_of_usages(self, obj):
        return obj.get_all_usages().count()
    
    
class ServiceUserDetailSerializer(serializers.ModelSerializer):
    total_usages = serializers.SerializerMethodField('get_number_of_usages', read_only=True)
    usages = serializers.SerializerMethodField("get_all_usages", read_only=True)
    
    class Meta:
        model = ServiceUser
        fields = ('id', 'full_name', 'phone', 'image', 'status', 'total_usages', 'usages')
    
    def get_number_of_usages(self, obj):
        return obj.get_all_usages().count()
    
    def get_all_usages(self, obj):
        return obj.get_all_usages()
    

class ServiceUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceUsage
        fields = '__all__'
        

class ServiseUsageDetailSerializer(serializers.ModelSerializer):
    user_data = ServiceUserSerializer(source='user')
    class Meta:
        model = ServiceUsage
        fields = (
            'id', 'user_data', 'is_done', 'description', 'created_at'
        )
        
    
class SocialMediaSerializer(serializers.ModelSerializer):
    total_interestors = serializers.SerializerMethodField('get_number_of_interestors')
    total_monthly_interestors = serializers.SerializerMethodField('get_number_of_monthly_interestors')
    total_weekly_interestors = serializers.SerializerMethodField('get_number_of_weekly_interestors')
    total_daily_interestors = serializers.SerializerMethodField('get_number_of_daily_interestors')
    
    class Meta:
        model = SocialMedia
        fields = (
            'id', 'name', 'followers', 'effect', 'description', 'created_at', 
            'total_interestors', 'total_monthly_interestors', 
            'total_weekly_interestors', 'total_daily_interestors',
            )
    
    def get_number_of_interestors(self, obj):
        return obj.get_all_interestors().count()
    
    def get_number_of_monthly_interestors(self, obj):
        return obj.get_this_month_interestors().count()
    
    def get_number_of_weekly_interestors(self, obj):
        return obj.get_this_week_interestors().count()
    
    def get_number_of_daily_interestors(self, obj):
        return obj.get_daily_interestors().count()        
    
        
class SocialMediaDetailSerializer(serializers.ModelSerializer):
    total_interestors = serializers.SerializerMethodField('get_number_of_interestors')
    total_monthly_interestors = serializers.SerializerMethodField('get_number_of_monthly_interestors')
    total_weekly_interestors = serializers.SerializerMethodField('get_number_of_weekly_interestors')
    total_daily_interestors = serializers.SerializerMethodField('get_number_of_daily_interestors')
    
    all_interestors = serializers.SerializerMethodField('get_all_interestors')
    monthly_interestors = serializers.SerializerMethodField('get_montly_interestors')
    weekly_interestors = serializers.SerializerMethodField("get_weekly_interestors")
    daily_interestors = serializers.SerializerMethodField("get_daily_interestors")
    
    class Meta:
        model = SocialMedia
        fields = (
            'id', 'name', 'followers', 'effect', 'description', 'created_at', 
            'total_interestors', 'total_monthly_interestors', 
            'total_weekly_interestors', 'total_daily_interestors',
            'all_interestors', 'monthly_interestors',
            'weekly_interestors', 'daily_interestors',
        )
    # Number of interestors are taking for data analyzing data and showing charts
    def get_number_of_interestors(self, obj):
        return obj.get_all_interestors().count()
    
    def get_number_of_monthly_interestors(self, obj):
        return obj.get_this_month_interestors().count()
    
    def get_number_of_weekly_interestors(self, obj):
        return obj.get_this_week_interestors().count()
    
    def get_number_of_daily_interestors(self, obj):
        return obj.get_daily_interestors().count()
    
    def get_all_interestors(self, obj):
        return obj.get_all_interestors()
    
    def get_montly_interestors(self, obj):
        return obj.get_this_month_interestors()
    
    def get_weekly_interestors(self, obj):
        return obj.get_this_week_interestors()
    
    def get_daily_interestors(self, obj):
        return obj.get_daily_interestors()
    
    
class InterestorsSerialer(serializers.ModelSerializer):     
    class Meta:
        model = Interestor
        fields = '__all__'


class InterestorDetailSerializer(serializers.ModelSerializer):
    found_us_where = serializers.SerializerMethodField('get_basic_data', read_only=True)
    class Meta:
        model = Interestor
        fields = ('id', 'first_name', 'last_name', 'phone', 'found_us_where', 'created_at')
    
    def get_basic_data(self, obj):
        """
        This function designed to get basic data 
        from Social Media which is Interestor Found_Us from

        Args:
            obj (_object_): This argument is Interestor's instance object
            context (_dictionary_): This argument collects all required data
        """
        context = {
            'id': obj.found_us.id,
            'name': obj.found_us.name,
            'followers': obj.found_us.followers,
            'created_at': obj.found_us.created_at
        }
        return context