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

# ***********************************************************************************
@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
@csrf_exempt
def all_departments(request):
    departments = Departments.objects.all()  # Use a different variable name
    departments_serializer = DepartmentSerializer(departments, many=True)
    if departments.exists():
        return JsonResponse(departments_serializer.data, safe=False)
    else:
        return JsonResponse("No data found", safe=True)


@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
)
@csrf_exempt
def department_by_id(request, id=1):
    departments = Departments.objects.filter(DepartmentID=id)
    departments_serializer = DepartmentSerializer(departments, many=True)
    if departments.exists():
        return JsonResponse(departments_serializer.data, safe=False)
    else:
        return JsonResponse('No data found', safe=False)


@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
@csrf_exempt
def all_employee(request, id=1):
    employees = Employee.objects.all()
    employees_serializer = EmployeeSerializer(employees, many=True)
    if employees.exists():
        return JsonResponse(employees_serializer.data, safe=False)
    else:
        return JsonResponse("No data found", safe=False)


@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
@csrf_exempt
def employee_by_id(request, id=1):
    employees = Employee.objects.filter(EmployeeID=id)
    employees_serializer = EmployeeSerializer(employees, many=True)
    if employees.exists():
        return JsonResponse(employees_serializer.data, safe=False)
    else:
        return JsonResponse("No data found", safe=False)


@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
@csrf_exempt
def employeedepartment(request, department_name):
    if request.method == 'GET':
        employees = Employee.objects.filter(Department=department_name)
        employee_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)


@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
@csrf_exempt
def add_department(request, id=0):
    try:
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)

        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        else:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500) @ api_view(['POST'])


@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
@csrf_exempt
def add_department(request, id=0):
    try:
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)

        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        else:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)


@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
@csrf_exempt
def add_employee(request):
    try:
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)

        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        else:
            return JsonResponse({'error': 'Invalid data provided'}, status=400)

    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)


@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
@csrf_exempt
def remove_department(request, id):
    department = Departments.objects.get(DepartmentID=id)
    if department.exists():
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    else:
        return JsonResponse("Data not found", safe=False)


@api_view(['POST'])
@swagger_auto_schema(
    operation_description="Retrieve a list of items.",
    responses={200: 'OK'},
)
@csrf_exempt
def remove_employee(request, id):
    employee = Employee.objects.get(EmployeeID=id)
    if employee.exists():
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    else:
        return JsonResponse("Data not found", status=200, safe=False)
