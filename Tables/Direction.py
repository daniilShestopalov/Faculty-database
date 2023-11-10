from django.db import models

from Tables.Department import Department


class Direction(models.Model):
    direction_id = models.AutoField(primary_key=True)
    direction_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100, null=True, default=None)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.direction_name} - {self.specialization}"
