from rest_framework import serializers

from .models import Schedule, Group

from students.serializers import StudentSerializer
from main.user_serializers import UserSerializer
from .schedule_serializers import ScheduleSerializer
# class ScheduleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = '__all__'
    
# class ScheduleDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = '__all__'

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
    

# class GroupDetailSerializer(serializers.ModelSerializer):
#     teacher_data = UserSerializer(source='teacher.user', read_only=True)
#     schedules = ScheduleSerializer(many=True, read_only=True)
#     students = StudentSerializer(many=True, read_only=True)
#     debtor_students = StudentSerializer(many=True, read_only=True)

#     class Meta:
#         model = Group
#         fields = ('id', 'subject', 'teacher_data', 'is_active', 'name',
#                   'price', 'description', 'created_at',
#                   'students', 'schedules', 'debtor_students')



#     def to_representation(self, instance):
#         instance.students = instance.get_all_students()
#         instance.schedules = instance.get_all_schedules()
#         instance.debtor_students = instance.get_debtor_students()
#         return super().to_representation(instance)