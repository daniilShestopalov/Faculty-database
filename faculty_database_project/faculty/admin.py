from django.contrib import admin
from .models import Curator, Department, Direction, Student, Group

admin.site.register(Curator)
admin.site.register(Direction)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Group)
