from rest_framework import serializers

from .models import Student, StudentPayment
from study.serializers import ScheduleSerializer
from main.serializers import UserSerializer

class StudentPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPayment
        fields = '__all__'
    

class StudentSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Student
        fields = (
            'id', 'user_data', 'is_active', 'balance', 'created_at'
        )
    
    

class StudentDetailSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)
    all_payments = serializers.SerializerMethodField()
    all_schedules = serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = (
            'id', 'user_data', 'is_active', 'balance', 'all_payments', 'all_schedules', 'created_at'
        )

    def get_all_schedules(self, obj):
        schedules = obj.get_all_schedules()
        return ScheduleSerializer(schedules, many=True, read_only=True).data
    
    def get_all_paymentss(self, obj):
        payments = obj.get_all_payments()
        return StudentPaymentSerializer(payments, many=True, read_only=True).data