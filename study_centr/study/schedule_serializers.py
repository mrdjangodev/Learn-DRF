from rest_framework import serializers

from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'
    
class ScheduleDetailSerializer(serializers.ModelSerializer):
    group_data = serializers.SerializerMethodField('get_group_data')
    
    class Meta:
        model = Schedule
        fields = (
            'id', 'room', 'group_data', 'is_active', 'start_time', 'finish_time',
        )
        
        
    def get_group_data(self, instance):
        group = instance.group
        data = {
            'id': group.id,
            'name': group.name,
            'techer':{
                'id': group.teacher.id,
                'username': group.teacher.user.username,
                'full_name': group.teacher.user.get_full_name(),
                'phone': group.teacher.user.phone
            },
            'is_active': group.is_active,
            'number_of_students': group.get_all_students().count(),
        }
        return data