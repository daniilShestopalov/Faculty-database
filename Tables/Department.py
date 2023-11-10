from django.db import models

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=100, unique=True)
    department_name_short = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f"{self.department_name} - {self.department_name_short}"


