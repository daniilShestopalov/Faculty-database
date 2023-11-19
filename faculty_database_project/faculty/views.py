from django.shortcuts import render, redirect

from faculty_database_project.faculty.models import Curator, Department, Direction, Group, Student


def home(request):
    return render(request, 'index.html')

def curator_list(request):
    curators = Curator.objects.all()
    return render(request, 'curators.html', {'curators': curators})

def delete_curator(request, curator_id):
    curator = Curator.objects.get(pk=curator_id)
    curator.delete()
    return redirect('curator_list')

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments.html', {'departments': departments})

def delete_department(request, department_id):
    department = Department.objects.get(pk=department_id)
    department.delete()
    return redirect('department_list')

def direction_list(request):
    directions = Direction.objects.all()
    return render(request, 'directions.html', {'directions': directions})

def delete_direction(request, direction_id):
    direction = Direction.objects.get(pk=direction_id)
    direction.delete()
    return redirect('direction_list')

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})

def delete_group(request, group_id):
    group = Group.objects.get(pk=group_id)
    group.delete()
    return redirect('group_list')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})

def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('student_list')


