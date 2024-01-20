from django.views.decorators.csrf import csrf_exempt
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from myapiapp.models import Departments, Employee
from myapiapp.serializers import DepartmentSerializer, EmployeeSerializer
from django.core.files.storage import default_storage
from rest_framework_swagger.views import get_swagger_view


@api_view(['GET', 'PUT', 'POST', 'DELETE'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()  # Use a different variable name
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentID=department_data['DepartmentID'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Updated", safe=False)
        return JsonResponse("Failed", safe=False)
    elif request.method == 'DELETE':  # Fix the method name to 'DELETE'
        department = Departments.objects.get(DepartmentID=id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)



@api_view(['GET', 'PUT', 'POST', 'DELETE'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        if id == 0:
            employees = Employee.objects.all()
            employee_serializer = EmployeeSerializer(employees, many=True)
            return JsonResponse(employee_serializer.data, safe=False)
        else:
            try:
                employee = Employee.objects.get(EmployeeID=id)
                employee_serializer = EmployeeSerializer(employee)
                return JsonResponse(employee_serializer.data, safe=False)
            except Employee.DoesNotExist:
                return JsonResponse({"error": "Employee not found"}, status=404)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeID=employee_data['EmployeeID'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated", safe=False)
        return JsonResponse("Failed", safe=False)
    elif request.method == 'DELETE':
        employee = Employee.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)


@csrf_exempt
def departmentEmployee(request, department_name):
    if request.method == 'GET':
        employees = Employee.objects.filter(Department=department_name)
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
