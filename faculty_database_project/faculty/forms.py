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


class CuratorForm(forms.ModelForm):
    class Meta:
        model = Curator
        fields = ['curator_second_name', 'curator_first_name', 'curator_middle_name', 'curator_contact_number']

    def clean_curator_second_name(self):
        curator_second_name = self.cleaned_data['curator_second_name']

        if not re.match(r'^[а-яА-ЯёЁ\s]+$', curator_second_name):
            raise ValidationError("Фамилия куратора должна содержать только русские буквы.")

        return curator_second_name

    def clean_curator_first_name(self):
        curator_first_name = self.cleaned_data['curator_first_name']

        if not re.match(r'^[а-яА-ЯёЁ\s]+$', curator_first_name):
            raise ValidationError("Имя куратора кафедры должно содержать только русские буквы.")

        return curator_first_name

    def clean_curator_middle_name(self):
        curator_middle_name = self.cleaned_data['curator_middle_name']
        if curator_middle_name is not None:
            if not re.match(r'^[а-яА-ЯёЁ\s]+$', curator_middle_name):
                raise ValidationError("Отчество куратора кафедры должно содержать только русские буквы.")

        return curator_middle_name

    def clean_curator_contact_number(self):
        curator_contact_number = self.cleaned_data['curator_contact_number']

        if not isinstance(curator_contact_number, (int, float)):
            raise ValidationError("Номер телефона должен быть числовым значением.")

            # Проверяем, что число начинается с '8' и состоит из 11 цифр
        if not re.match(r'^8\d{10}$', str(curator_contact_number)):
            raise ValidationError("Номер телефона должен начинаться с '8' и состоять из 11 цифр.")

        return curator_contact_number


class DirectionForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = ['direction_name', 'specialization', 'department']

    def clean_direction_name(self):
        direction_name = self.cleaned_data['direction_name']

        if not re.match(r'^[а-яА-ЯёЁ\s]+$', direction_name):
            raise ValidationError("Название направления должно содержать только русские буквы.")

        return direction_name

    def clean_specialization(self):
        specialization = self.cleaned_data['specialization']
        if specialization is not None:
            if not re.match(r'^[а-яА-ЯёЁ\s]+$', specialization):
                raise ValidationError("Специализация направления должна содержать только русские буквы.")

        return specialization


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['group_number', 'group_course_number', 'direction', 'curator', 'group_leader']

    def clean_group_number(self):
        group_number = self.cleaned_data['group_number']
        try:
            group_number_int = int(group_number)
            if group_number_int <= 0:
                raise ValidationError("Номер группы должен быть положительным целым числом.")
        except ValueError:
            raise ValidationError("Номер группы должен быть целым числом.")
        return group_number

    def clean_group_course_number(self):
        group_course_number = self.cleaned_data['group_course_number']
        try:
            group_course_number_int = int(group_course_number)
            if group_course_number_int <= 0 or group_course_number_int > 6:
                raise ValidationError("Номер курса группы должен быть целым числом от 1 до 6.")
        except ValueError:
            raise ValidationError("Номер курса группы должен быть целым числом.")
        return group_course_number

    def clean(self):
        cleaned_data = super().clean()
        group_number = cleaned_data.get('group_number')
        group_course_number = cleaned_data.get('group_course_number')

        if self.instance.pk is None:
            if Group.objects.filter(group_number=group_number, group_course_number=group_course_number).exists():
                raise ValidationError("Группа с таким номером курса и номером группы уже существует.")
        else:
            if Group.objects.filter(group_number=group_number, group_course_number=group_course_number).exclude(
                    pk=self.instance.pk).exists():
                raise ValidationError("Другая группа с таким номером курса и номером группы уже существует.")

        return cleaned_data


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_second_name', 'student_first_name', 'student_middle_name', 'group', 'student_status']

    def clean_student_second_name(self):
        student_second_name = self.cleaned_data['student_second_name']

        if not re.match(r'^[а-яА-ЯёЁ\s]+$', student_second_name):
            raise ValidationError("Фамилия студента должна содержать только русские буквы.")

        return student_second_name

    def clean_student_first_name(self):
        student_first_name = self.cleaned_data['student_first_name']

        if not re.match(r'^[а-яА-ЯёЁ\s]+$', student_first_name):
            raise ValidationError("Имя студента должно содержать только русские буквы.")

        return student_first_name

    def clean_student_middle_name(self):
        student_middle_name = self.cleaned_data['student_middle_name']
        if student_middle_name is not None:
            if not re.match(r'^[а-яА-ЯёЁ\s]+$', student_middle_name):
                raise ValidationError("Отчество студента должно содержать только русские буквы.")

        return student_middle_name

    def clean_student_status(self):
        student_status = self.cleaned_data['student_status']

        valid_statuses = [choice[0] for choice in Student.STUDENT_STATUS_CHOICES]

        if student_status not in valid_statuses:
            raise ValidationError("Недопустимый статус студента. Выберите корректный статус.")

        return student_status
