from rest_framework import serializers

from .models import Student, StudentPayment
from main.models import CustomUser
from employee.admin_serializers import AdminstratorsSerializer
from study.schedule_serializers import ScheduleSerializer
from main.user_serializers import UserSerializer


class StudentSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user')
    
    class Meta:
        model = Student
        fields = (
            'id', 'user_data', 'is_active', 'balance', 'created_at'
        )

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = CustomUser.objects.create(**user_data)
        student = Student.objects.create(user=user, **validated_data)
        return student
    
class StudentPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPayment
        fields = '__all__'


class StudentPaymentDetailSerializer(serializers.ModelSerializer):
    adminstrator_detail = AdminstratorsSerializer(source="adminstrator", read_only=True)
    student_detail = StudentSerializer(source='student', read_only=True)
    # student = serializers.ChoiceField(choices=Student.objects.all(), write_only=True)
    class Meta:
        model = StudentPayment
        fields = (
            'id', 'adminstrator_data', 'student_data','amount', 'created_at',
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