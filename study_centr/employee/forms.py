from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['id', 'user', 'is_active', 'salary', 'subjects']
        widgets = {
            'subjects': forms.CheckboxSelectMultiple
        }