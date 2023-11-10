from django.db import models

from Tables.Curator import Curator
from Tables.Direction import Direction
from Tables.Student import Student


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_number = models.IntegerField()
    group_course_number = models.IntegerField()
    direction_id = models.ForeignKey(Direction, on_delete=models.CASCADE)
    curator_id = models.ForeignKey(Curator, on_delete=models.CASCADE, null=True, default=None, unique=True)
    group_leader_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, default=None)

    def __str__(self):
        return f"Group {self.group_number} - Course {self.group_course_number}"