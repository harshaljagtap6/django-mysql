
from django.urls import re_path
from myapiapp import views
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf import settings

urlpatterns = [
            re_path(r'^all_departments/$', AllDepartments.as_view()), #done
            re_path(r'^department/$', DepartmentById.as_view()), #done
            re_path(r'^add_department/$', AddDepartment.as_view()), #done
            re_path(r'^remove_department/$', RemoveDepartment.as_view()), #done
            re_path(r'^all_employees/$', AllEmployees.as_view()), #done
            re_path(r'^employee/$', EmployeeById.as_view()), #done
            re_path(r'^add_employee/$', AddEmployee.as_view()), #done
            re_path(r'^remove_employee/$', RemoveEmployee.as_view()), #done
            re_path(r'^employees_of_department/$', EmployeeOfDepartment.as_view())
]
