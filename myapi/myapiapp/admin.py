from django.contrib import admin

from myapiapp.models import Departments, Employee

admin.site.register([Departments, Employee])

# Register your models here.
