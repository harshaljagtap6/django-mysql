from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from myapiapp.models import Departments, Employee
from myapiapp.serializers import DepartmentSerializer, EmployeeSerializer
from rest_framework.views import APIView
from .models import *
from .serializers import *

class AllDepartments(APIView):
        
    def post(self, request, *args, **kwargs):
        data = Departments.objects.all()
        if not data.exists():
            return Response({"detail": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(data=data, many=True)
        # Call is_valid before accessing serialized data
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
class DepartmentById(APIView):

    @swagger_auto_schema(
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'DepartmentId': openapi.Schema(type=openapi.TYPE_INTEGER),
                },
                required=['DepartmentId'],
            ),
            responses={
                201: "Success",
                400: "Bad request"
            },
            operation_id="show_department",
            operation_description="Show particular department",
    )
    def post(self, request, *args, **kwargs):
        department_id = request.data.get('DepartmentId')
        data = Departments.objects.filter(DepartmentID=department_id)
        if not data.exists():
            return Response({"detail": "Department not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = DepartmentSerializer(data=data, many=True)
        
        # Call is_valid before accessing serialized data
        serializer.is_valid()

        return Response(serializer.data, status=status.HTTP_200_OK)



class AddDepartment(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'DepartmentName': openapi.Schema(type=openapi.TYPE_STRING),
                # Add other properties as needed
            },
            example={'DepartmentName': 'IT'},
            required=['DepartmentName'],  # Specify required fields
        ),
        responses={
            201: "Success",
            400: "Bad Request",
        },
        operation_id="add_department",
        tags=["add_department"],
    )
    def post(self, request, *args, **kwargs):
        # Extract parameters from request
        department_name = request.data.get('DepartmentName')

        # You can perform any logic with the parameters here

        data = {
            'DepartmentName': department_name,
        }

        serializer = DepartmentSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Department has been added", safe=False)

        return JsonResponse("Department has been added", safe=False)
        

class RemoveDepartment(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'DepartmentId': openapi.Schema(type=openapi.TYPE_INTEGER),
                # Add other properties as needed
            },
            required=['DepartmentId'],  # Specify required fields
        ),
        responses={
            201: "Success",
            400: "Bad Request",
        },
        operation_id="remove_department",
        tags=["remove_department"],
    )
    def post( self, request, *args, **kwargs):
        id = request.data.get('DepartmentId')
        department = Departments.objects.filter(DepartmentID=id)
        if department.exists():
            department.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        else:
            return JsonResponse("Data not found", safe=False)

class AllEmployees(APIView):

    def post(self, request, *args, **kwargs):
        data = Employee.objects.all()
        if not data.exists():
            return Response({"detail": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(data=data, many=True)
        # Call is_valid before accessing serialized data
        serializer.is_valid()
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class EmployeeById(APIView):

    @swagger_auto_schema(
            request_body=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'EmployeeId': openapi.Schema(type=openapi.TYPE_INTEGER),
                },
                required=['EmployeeId'],
            ),
            responses={
                201: "Success",
                400: "Bad request"
            },
            operation_id="show_employee",
            operation_description="Show particular employee",
    )
    def post(self, request, *args, **kwargs):
        employee_id = request.data.get('EmployeeId')
        data = Employee.objects.filter(EmployeeID=employee_id)
        if not data.exists():
            return Response({"detail": "Employee not found please check EmployeeId"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(data=data, many=True)
        
        # Call is_valid before accessing serialized data
        serializer.is_valid()

        return Response(serializer.data, status=status.HTTP_200_OK)



class AddEmployee(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'EmployeeId': openapi.Schema(type=openapi.TYPE_INTEGER),
                'EmployeeName': openapi.Schema(type=openapi.TYPE_STRING),
                'Department': openapi.Schema(type=openapi.TYPE_STRING),
                'DateOfJoining': openapi.Schema(type=openapi.TYPE_STRING),
                'PhotoFieldName': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['EmployeeName', 'Department'], 
            example={
                "EmployeeId": 69,
                "EmployeeName": "John",
                "Department": "Doe",
                "DateOfJoining": "yyyy-mm-dd",
                "PhotoFieldName": "string"
            }
        ),
        responses={
            201: "Success",
            400: "Bad Request",
        },
        operation_id="add_employee",
        tags=["add_employee"],
    )
    def post(self, request, *args, **kwargs):
        # Extract parameters from request
        EmployeeId = request.data.get('EmployeeId')
        EmployeeName = request.data.get('EmployeeName')
        Department = request.data.get('Department')
        DateOfJoining = request.data.get('DateOfJoining')
        PhotoFieldName = request.data.get('PhotoFieldName')

        # You can perform any logic with the parameters here

        data = {
            "EmployeeID": EmployeeId,
            "EmployeeName": EmployeeName,
            "Department": Department,
            "DateOfJoining": DateOfJoining,
            "PhotoFieldName": PhotoFieldName
        }

        serializer = EmployeeSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Employee has been added", safe=False)

        return JsonResponse("Employee has not been added please check your input.", safe=False)

class RemoveEmployee(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'EmployeeId': openapi.Schema(type=openapi.TYPE_INTEGER),
                # Add other properties as needed
            },
            required=['EmployeeId'],  # Specify required fields
        ),
        responses={
            201: "Success",
            400: "Bad Request",
        },
        operation_id="remove_employee",
        tags=["remove_employee"],
    )
    def post( self, request, *args, **kwargs):
        id = request.data.get('EmployeeId')
        employee = Employee.objects.filter(EmployeeID=id)
        if employee.exists():
            employee.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        else:
            return JsonResponse("Data not found", safe=False)


class EmployeeOfDepartment(APIView):

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'DepartmentId': openapi.Schema(type=openapi.TYPE_STRING),
            },
            required=['DepartmentId'],
        ),
        responses={
            201: "Success",
            400: "Bad request"
        },
        operation_id="show_employee",
        operation_description="Show particular employee",
    )
    def post(self, request, *args, **kwargs):
        department = request.data.get('DepartmentId')
        data = Employee.objects.filter(Department=department)
        if not data.exists():
            return Response({"detail": "Employee(s) not found please check DepartmentId"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(data=data, many=True)
        
        # Call is_valid before accessing serialized data
        serializer.is_valid()

        return Response(serializer.data, status=status.HTTP_200_OK)
