from rest_framework import serializers

from .models import Schedule, Group

from students.serializers import StudentSerializer
from main.serializers import UserSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
        

# class GroupSerializer(serializers.ModelSerializer):
#     teacher_data = UserSerializer(source='teacher.user', read_only=True)
#     all_schedules = serializers.SerializerMethodField()
#     all_students = serializers.SerializerMethodField()
#     all_debtor_students = serializers.SerializerMethodField()
#     class Meta:
#         model = Group
#         fields = ('id', 'subject', 'teacher_data', 'is_active', 'name', 
#                   'price', 'description', 'created_at', 
#                   'all_students', 'all_schedules', 'all_debtor_students')        
        
#     def get_all_schedules(self, obj):
#         schedules = obj.get_all_schedules()
#         return ScheduleSerializer(schedules, many=True).data
    
#     def get_all_students(self, obj):
#         students = obj.get_all_students()
#         return StudentSerializer(students, many=True).data
    
#     def get_debtor_students(self, obj):
#         debtors = obj.get_debtor_students()
#         return StudentSerializer(debtors, many=True).data
    

class GroupSerializer(serializers.ModelSerializer):
    teacher_data = UserSerializer(source='teacher.user', read_only=True)
    schedules = ScheduleSerializer(many=True, read_only=True)
    students = StudentSerializer(many=True, read_only=True)
    debtor_students = StudentSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'subject', 'teacher_data', 'is_active', 'name',
                  'price', 'description', 'created_at',
                  'students', 'schedules', 'debtor_students')

    def to_representation(self, instance):
        instance.students = instance.get_all_students()
        instance.schedules = instance.get_all_schedules()
        instance.debtor_students = instance.get_debtor_students()
        return super().to_representation(instance)