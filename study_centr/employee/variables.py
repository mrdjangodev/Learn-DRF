

employees_permissions = {
    'boss': (
            ('can_view_boss', 'Can view boss'),
            ('can_add_boss', 'Can add boss'),
            ('can_change_boss', 'Can change boss'),
            ('can_delete_boss', 'Can delete boss'),
            
            ('can_view_teacher', "Can view teacher"),
            ('can_add_teacher', 'Can add teacher'),
            ('can_change_teacher', 'Can change teacher'),
            # ('can_delete_teacher', 'Can delete teacher'),
            
            ('can_view_adminstrator', "Can view adminstrator"),
            ('can_add_adminstrator', 'Can add adminstrator'),
            ('can_change_adminstrator', 'Can change adminstrator'),
            ('can_delete_adminstrator', 'Can delete adminstrator'),
            
            ('can_view_accountant', "Can view accountant"),
            ('can_add_accountant', 'Can add accountant'),
            ('can_change_accountant', 'Can change accountant'),
            ('can_delete_accountant', 'Can delete accountant'),
            
            ('can_view_services', 'Can view services'),
            ('can_view_subjects', 'Can view subjects'),
            ('can_view_groups', 'Can view groups'),
        ),
    
    
    'adminstrator': (
        ('can_view_teacher', "Can view teacher"),
        ('can_add_teacher', 'Can add teacher'),
        ('can_change_teacher', 'Can change teacher'),

        ('can_view_student', "Can view student"),
        ('can_add_student', 'Can add student'),
        ('can_change_student', 'Can change student'),
        
        ('can_view_studentpayment', "Can view studentpayment"),
        ('can_add_studentpayment', 'Can add studentpayment'),
        
        ('can_view_room', "Can view room"),
        ('can_add_room', 'Can add room'),
        ('can_change_room', 'Can change room'),
        
        ('can_view_subject', "Can view subject"),
        ('can_add_subject', 'Can add subject'),
        ('can_change_subject', 'Can change subject'),
        
        ('can_view_group', "Can view group"),
        ('can_add_group', 'Can add group'),
        ('can_change_group', 'Can change group'),
        
        ('can_view_socialmedia', "Can view social media"),
        ('can_add_socialmedia', 'Can add social media'),
        ('can_change_socialmedia', 'Can change social media'),
        
        ('can_view_service', "Can view service"),
        ('can_add_service', 'Can add service'),
        ('can_change_service', 'Can change service'),
        
        ('can_view_serviceuser', "Can view serviceuser"),
        ('can_add_serviceuser', 'Can add serviceuser'),
        
        ('can_view_serviceusage', "Can view serviceusage"),
        ('can_add_serviceusage', 'Can add serviceusage'),
        ('can_change_serviceusage', 'Can change serviceusage'),
        
        ('can_view_schedule', "Can view schedule"),
        ('can_add_schedule', 'Can add schedule'),
        ('can_change_schedule', 'Can change schedule'),
        ('can_delete_schedule', 'Can delete schedule'),
        
        ('can_view_servicepayment', "Can view servicepayment"),
        ('can_add_servicepayment', 'Can add servicepayment'),
        
        ('can_view_interestor', "Can view interestor"),          
    ),
    
    'teacher': (),
    'accountant': (),
}

# from django.contrib.auth.models import Permission
# print(Permission.objects.filter(name__icontains="servicepayment"))