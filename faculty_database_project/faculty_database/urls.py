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
from django.contrib import admin
from django.urls import path
from django.urls import path
from faculty_database_project.faculty import views
from faculty_database_project.faculty.views import curator_list, delete_curator

'''urlpatterns = [
    path('admin/', admin.site.urls),
]'''

urlpatterns = [
    path('', views.home, name='home'),
    path('curators/', curator_list, name='curator_list'),
    path('curators/delete/<int:curator_id>/', delete_curator, name='curator_delete'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/delete/<int:department_id>/', views.delete_department, name='delete_department'),
    path('directions/', views.direction_list, name='direction_list'),
    path('directions/delete/<int:direction_id>/', views.delete_direction, name='delete_direction'),
    path('groups/', views.group_list, name='group_list'),
    path('groups/delete/<int:group_id>/', views.delete_group, name='delete_group'),
    path('students/', views.student_list, name='student_list'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),

]
