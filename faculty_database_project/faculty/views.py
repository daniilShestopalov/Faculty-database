from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import DepartmentForm, CuratorForm, DirectionForm, GroupForm, StudentForm
from .models import Curator, Department, Direction, Student, Group


def home(request):
    return render(request, 'index.html')


def curator_list(request):
    curators = Curator.objects.order_by('curator_id')
    count = curators.count()
    pages = Paginator(curators, 25)
    page_number = request.GET.get('page')
    try:
        page_curators = pages.get_page(page_number)
    except PageNotAnInteger:
        page_curators = pages.page(1)
    except EmptyPage:
        page_curators = pages.page(pages.num_pages)
    return render(request, 'curators.html', {'page_curators': page_curators, 'count': count})


def curator_add(request):
    return render(request, 'curator_add.html')


def curator_add_confirm(request):
    if request.method == 'POST':
        form = CuratorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Куратор успешно добавлен.')
            return redirect('curator_list')
        else:
            errors = []
            for field, error_messages in form.errors.items():
                field_label = form.fields[field].label
                for error in error_messages:
                    errors.append(f"{field_label}: {error}")
            messages.error(request, '\n'.join(errors))

        return curator_add(request)


def curator_change(request, curator_id):
    curator = Curator.objects.get(pk=curator_id)
    return render(request, 'curator_change.html', {'curator': curator})


def curator_change_confirm(request, curator_id):
    curator = Curator.objects.get(pk=curator_id)
    if request.method == 'POST':
        form = CuratorForm(request.POST, instance=curator)
        if form.is_valid():
            form.save()
            messages.success(request, 'Куратор успешно изменен.')
            return redirect('curator_list')
        else:
            errors = []
            for field, error_messages in form.errors.items():
                field_label = form.fields[field].label
                for error in error_messages:
                    errors.append(f"{field_label}: {error}")
            messages.error(request, '\n'.join(errors))

    return curator_change(request, curator_id)


def delete_curator(request, curator_id):
    curator = Curator.objects.get(pk=curator_id)
    curator.delete()
    return redirect('curator_list')


def department_list(request):
    departments = Department.objects.order_by('department_id')
    count = departments.count()
    pages = Paginator(departments, 10)
    page_number = request.GET.get('page')
    try:
        page_departments = pages.get_page(page_number)
    except PageNotAnInteger:
        page_departments = pages.page(1)
    except EmptyPage:
        page_departments = pages.page(pages.num_pages)
    return render(request, 'departments.html', {'page_departments': page_departments, 'count': count})


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
            errors = []
            for field, error_messages in form.errors.items():
                field_label = form.fields[field].label
                for error in error_messages:
                    errors.append(f"{field_label}: {error}")
            messages.error(request, '\n'.join(errors))

    return department_add(request)


def department_change(request, department_id):
    department = Department.objects.get(pk=department_id)
    return render(request, 'departmental_change.html', {'department': department})


def department_change_confirm(request, department_id):
    department = Department.objects.get(pk=department_id)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            messages.success(request, 'Кафедра успешно изменена.')
            return redirect('department_list')
        else:
            errors = []
            for field, error_messages in form.errors.items():
                field_label = form.fields[field].label
                for error in error_messages:
                    errors.append(f"{field_label}: {error}")
            messages.error(request, '\n'.join(errors))

    return department_change(request, department_id)


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
    count = directions.count()
    pages = Paginator(directions, 10)
    page_number = request.GET.get('page')
    try:
        page_direction = pages.get_page(page_number)
    except PageNotAnInteger:
        page_direction = pages.page(1)
    except EmptyPage:
        page_direction = pages.page(pages.num_pages)

    return render(request, 'directions.html', {'page_direction': page_direction, 'count': count})


def direction_add(request):
    departments = Department.objects.all()
    return render(request, 'direction_add.html', {'departments': departments})


def direction_add_confirm(request):
    if request.method == 'POST':
        form = DirectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Направление успешно добавлена.')
            return redirect('direction_list')
        else:
            errors = []
            for field, error_messages in form.errors.items():
                field_label = form.fields[field].label
                for error in error_messages:
                    errors.append(f"{field_label}: {error}")
            messages.error(request, '\n'.join(errors))

    return direction_add(request)


def direction_change(request, direction_id):
    departments = Department.objects.all()
    direction = Direction.objects.get(pk=direction_id)
    return render(request, 'direction_change.html', {'departments': departments, 'direction': direction})


def direction_change_confirm(request, direction_id):
    direction = Direction.objects.get(pk=direction_id)
    if request.method == 'POST':
        form = DirectionForm(request.POST, instance=direction)
        if form.is_valid():
            form.save()
            messages.success(request, 'Направление успешно изменено.')
            return redirect('direction_list')
        else:
            errors = []
            for field, error_messages in form.errors.items():
                field_label = form.fields[field].label
                for error in error_messages:
                    errors.append(f"{field_label}: {error}")
            messages.error(request, '\n'.join(errors))

    return direction_change(request, direction_id)


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
    count = groups.count()
    pages = Paginator(groups, 10)
    page_number = request.GET.get('page')
    try:
        page_group = pages.get_page(page_number)
    except PageNotAnInteger:
        page_group = pages.page(1)
    except EmptyPage:
        page_group = pages.page(pages.num_pages)
    return render(request, 'groups.html', {'page_group': page_group, 'count': count})


def group_add(request):
    curators = Curator.objects.all()
    directions = Direction.objects.all()
    return render(request, 'group_add.html', {'curators': curators, 'directions': directions})


def group_add_confirm(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.group_leader = None
            group.save()
            form.save_m2m()
            messages.success(request, 'Группа успешно добавлена.')
            return redirect('group_list')
        else:
            errors = []
            for field, error_messages in form.errors.items():
                if field == '__all__':
                    errors.extend(error_messages)
                else:
                    field_label = form.fields[field].label or field
                    for error in error_messages:
                        errors.append(f"{field_label}: {error}")
            messages.error(request, '\n'.join(errors))

    return group_add(request)


def group_change(request, group_id):
    curators = Curator.objects.all()
    directions = Direction.objects.all()
    students = Student.objects.filter(group=group_id)
    group = Group.objects.get(pk=group_id)
    return render(request, 'group_change.html',
                  {'group': group, 'curators': curators, 'directions': directions, 'students': students})


def group_change_confirm(request, group_id):
    group = Group.objects.get(pk=group_id)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, 'Группа успешно изменено.')
            return redirect('group_list')
        else:
            errors = []
            for field, error_messages in form.errors.items():
                if field == '__all__':
                    errors.extend(error_messages)
                else:
                    field_label = form.fields[field].label or field
                    for error in error_messages:
                        errors.append(f"{field_label}: {error}")
            messages.error(request, '\n'.join(errors))

    return group_change(request, group_id)


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
    students = Student.objects.order_by('student_id')
    count = students.count()
    pages = Paginator(students, 25)
    page_number = request.GET.get('page')
    try:
        page_students = pages.get_page(page_number)
    except PageNotAnInteger:
        page_students = pages.page(1)
    except EmptyPage:
        page_students = pages.page(pages.num_pages)
    return render(request, 'students.html', {'page_students': page_students, 'count': count})


def student_add(request):
    student_statuses = Student.STUDENT_STATUS_CHOICES
    groups = Group.objects.all()
    return render(request, 'student_add.html', {'student_statuses': student_statuses, 'groups': groups})


def student_add_confirm(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Студент успешно добавлен.')
            return redirect('student_list')
        else:
            errors = []
            for field, error_messages in form.errors.items():
                if field == '__all__':
                    errors.extend(error_messages)
                else:
                    field_label = form.fields[field].label or field
                    for error in error_messages:
                        errors.append(f"{field_label}: {error}")
            messages.error(request, '\n'.join(errors))

    return group_add(request)


def student_change(request, student_id):
    student = Student.objects.get(pk=student_id)
    groups = Group.objects.all()
    student_statuses = Student.STUDENT_STATUS_CHOICES
    return render(request, 'student_change.html',
                  {'groups': groups, 'student': student, 'student_statuses': student_statuses})


def student_change_confirm(request, student_id):
    student = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Студент успешно изменен.')
            return redirect('student_list')
        else:
            errors = []
            for field, error_messages in form.errors.items():
                if field == '__all__':
                    errors.extend(error_messages)
                else:
                    field_label = form.fields[field].label or field
                    for error in error_messages:
                        errors.append(f"{field_label}: {error}")
            messages.error(request, '\n'.join(errors))

    return student_change(request, student_id)


def delete_student(request, student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('student_list')
