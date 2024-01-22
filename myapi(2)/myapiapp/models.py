from django.db import models

# Create your models here.

class Departments(models.Model):
    objects = None
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

    def __str__(self):
        return str(str(self.DepartmentID) + " " + self.DepartmentName)

class Employee(models.Model):
    objects = None
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField()
    PhotoFieldName = models.CharField(max_length=500)