from rest_framework import serializers
from .models import*

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields='__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'