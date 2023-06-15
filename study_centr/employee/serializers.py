from rest_framework import serializers

from .models import Teacher, Adminstrator, Accountant, Boss


class BossesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        filds = '__all__'
    

class BossDetail(serializers.ModelSerializer):
    class Meta:
        model = Boss
        filds = '__all__'
    
    

