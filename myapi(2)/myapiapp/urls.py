from django.urls import include, re_path
from myapiapp import views
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  re_path(r'^all_departments$', views.all_departments),
                  re_path(r'^department/([0-9]+)$', views.department_by_id),
                  re_path(r'^add_department/$', views.add_department),
                  re_path(r'^remove_department/([0-9]+)$', views.remove_department),
                  re_path(r'^all_employees$', views.all_employee),
                  re_path(r'^employee/([0-9]+)$', views.employee_by_id),
                  re_path(r'^add_employee/$', views.add_employee),
                  re_path(r'^remove_employee/([0-9]+)$', views.remove_employee),
                  re_path(r'^employees_of_department/(?P<department_name>\w+)$', views.employeedepartment)
              ]
