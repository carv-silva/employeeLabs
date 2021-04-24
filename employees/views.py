from rest_framework import viewsets
from employees.models import Employee
from employees.serializer import EmployeeSerializer


# exibindo os funcionarios
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
