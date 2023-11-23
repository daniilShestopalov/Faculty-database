from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse

from .forms import DepartmentForm
from .models import Curator, Department, Direction, Student, Group


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


def department_add(request):
    return render(request, 'department_add.html')


def department_add_confirm(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Кафедра успешно добавлена.')
            return redirect('department_list')
        else:
            messages.error(request, 'В форме обнаружены ошибки.')
    else:
        form = DepartmentForm()

    return render(request, 'departments/department_add.html', {'form': form})


def delete_department(request, department_id):
    try:
        department = Department.objects.get(pk=department_id)
        department.delete()
        return HttpResponseRedirect(reverse('department_list'))
    except IntegrityError:
        messages.error(request, 'Нельзя удалить кафедру, у которой есть направления.')
        return HttpResponseRedirect(reverse('department_list'))
    except Exception as e:
        messages.error(request, f'Произошла неожиданная ошибка: {e}')
        return HttpResponseRedirect(reverse('department_list'))


def direction_list(request):
    directions = Direction.objects.all()
    return render(request, 'directions.html', {'directions': directions})


def delete_direction(request, direction_id):
    try:
        direction = Direction.objects.get(pk=direction_id)
        direction.delete()
        return HttpResponseRedirect(reverse('direction_list'))
    except IntegrityError:
        messages.error(request, 'Нельзя удалить направление, у которой есть группы.')
        return HttpResponseRedirect(reverse('direction_list'))
    except Exception as e:
        messages.error(request, f'Произошла неожиданная ошибка: {e}')
        return HttpResponseRedirect(reverse('direction_list'))


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})


def delete_group(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
        group.delete()
        return HttpResponseRedirect(reverse('group_list'))
    except IntegrityError:
        messages.error(request, 'Нельзя удалить группу, у которой есть студенты.')
        return HttpResponseRedirect(reverse('group_list'))
    except Exception as e:
        messages.error(request, f'Произошла неожиданная ошибка: {e}')
        return HttpResponseRedirect(reverse('group_list'))


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('student_list')
