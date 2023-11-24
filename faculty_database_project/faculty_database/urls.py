"""
URL configuration for faculty_database project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from faculty import views


urlpatterns = [
    path('', views.home, name='home'),
    path('curators/', views.curator_list, name='curator_list'),
    path('curators/delete/<int:curator_id>/', views.delete_curator, name='curator_delete'),
    path('curators/add/', views.curator_add, name='curator_add'),
    path('curators/add/confirm/', views.curator_add_confirm, name='curator_add_confirm'),
    path('curators/change/<int:curator_id>/', views.curator_change, name='curator_change'),
    path('curators/change/<int:curator_id>/confirm/', views.curator_change_confirm, name='curator_change_confirm'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/delete/<int:department_id>/', views.delete_department, name='department_delete'),
    path('departments/add/', views.department_add, name='department_add'),
    path('departments/add/confirm/', views.department_add_confirm, name='department_add_confirm'),
    path('departments/change/<int:department_id>/', views.department_change, name='department_change'),
    path('departments/change/<int:department_id>/confirm/', views.department_change_confirm, name='department_change_confirm'),
    path('directions/', views.direction_list, name='direction_list'),
    path('directions/delete/<int:direction_id>/', views.delete_direction, name='direction_delete'),
    path('direction/add/', views.direction_add, name='direction_add'),
    path('direction/add/confirm/', views.direction_add_confirm, name='direction_add_confirm'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/delete/<int:group_id>/', views.delete_group, name='group_delete'),
    path('students/', views.student_list, name='student_list'),
    path('students/delete/<int:student_id>/', views.delete_student, name='student_delete'),
]

