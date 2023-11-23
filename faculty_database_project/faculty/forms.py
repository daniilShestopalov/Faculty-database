import re

from django import forms
from django.core.exceptions import ValidationError

from .models import Department, Direction, Student, Group, Curator

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name', 'department_name_short']

    def clean_department_name(self):
        department_name = self.cleaned_data['department_name']

        if not re.match(r'^[а-яА-ЯёЁ\s]+$', department_name):
            raise ValidationError("Название кафедры должно содержать только русские буквы.")

        return department_name

    def clean_department_name_short(self):
        department_name_short = self.cleaned_data['department_name_short']

        if not re.match(r'^[а-яА-ЯёЁ\s]+$', department_name_short):
            raise ValidationError("Сокращенное название кафедры должно содержать только русские буквы.")

        return department_name_short