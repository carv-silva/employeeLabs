from rest_framework import viewsets
from django.views.generic import ListView
from employees.models import Employee, Department, Payroll
from employees.serializer import EmployeeSerializer, DepartmentSerializer, PayrollSerializer


# exibindo os funcionarios
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# exibindo departamento
class DepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


# exibindo folha de pagamento
class PayrollsViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer


'''# listando Payroll
class PayrollsListView(ListView):
    model = Payroll
'''