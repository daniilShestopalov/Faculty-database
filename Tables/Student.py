from django.db import models
from django.utils.translation import gettext_lazy as _

from Tables.Group import Group

class StudentStatus(models.TextChoices):
    STUDY = 'study', _('Study')
    ALUMNUS = 'alumnus', _('Alumnus')
    EXPELLED = 'expelled', _('Expelled')

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_second_name = models.CharField(max_length=45)
    student_first_name = models.CharField(max_length=45)
    student_middle_name = models.CharField(max_length=45, null=True, default=None)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    student_status = models.CharField(max_length=8, choices=StudentStatus.choices, default=StudentStatus.STUDY)

def __str__(self):
    full_name = f"{self.student_second_name} {self.student_first_name}"
    if self.student_middle_name:
        full_name += f" {self.student_middle_name}"
    return f"{full_name} ({self.student_status})"
