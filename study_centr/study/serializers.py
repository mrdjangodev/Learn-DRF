from rest_framework import serializers

from .models import Schedule, Group

from students.serializers import StudentSerializer
from main.user_serializers import UserSerializer
from .schedule_serializers import ScheduleSerializer

class GroupSerializer(serializers.ModelSerializer):
    teacher_data = UserSerializer(source='teacher.user', read_only=True)
    class Meta:
        model = Group
        fields = ('id', 'subject', 'teacher_data', 'is_active', 'created_at')
    
 
class GroupDetailSerializer(serializers.ModelSerializer):
    debtor_students = serializers.SerializerMethodField('get_debtor_students')
    all_students = serializers.SerializerMethodField('get_all_students')
    active_students = serializers.SerializerMethodField('get_all_active_students')
    schedules = serializers.SerializerMethodField('get_all_schedules')

    class Meta:
        model = Group
        fields = ('id', 'subject', 'teacher', 'is_active', 'name', 'price', 'description', 'created_at', 'debtor_students', 'all_students', 'active_students', 'schedules')
        read_only_fields = ('created_at', 'debtor_students', 'all_students', 'active_students', 'schedules')

    def get_debtor_students(self, obj):
        debtor_students = obj.students_set.filter(balance__lt=0)
        return StudentSerializer(debtor_students, many=True).data

    def get_all_students(self, obj):
        all_students = obj.students_set.all()
        return StudentSerializer(all_students, many=True).data

    def get_all_active_students(self, obj):
        active_students = obj.students_set.filter(is_active=True)
        return StudentSerializer(active_students, many=True).data

    def get_all_schedules(self, obj):
        schedules = obj.schedule_set.all()
        return ScheduleSerializer(schedules, many=True).data 
    

