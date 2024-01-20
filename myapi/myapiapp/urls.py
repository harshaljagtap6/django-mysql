from django.urls import include, re_path
from myapiapp import views
from .views import *
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^department$', views.departmentApi),
    re_path(r'^department/([0-9]+$)',views.departmentApi),
    re_path(r'^employee$', views.employeeApi),
    re_path(r'^employee/([0-9]+$)',views.employeeApi),
    re_path(r'^employee/SaveFile',views.SaveFile),
    re_path(r'^department/employee/(?P<department_name>\w+)$', views.departmentEmployee)
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)