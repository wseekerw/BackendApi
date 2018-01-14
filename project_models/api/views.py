from rest_framework.generics import ListCreateAPIView
from rest_framework import permissions
from .serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.permissions import AllowAny


from project_models.models import Department, Employee


class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class DepartmentListCreateAPIView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

