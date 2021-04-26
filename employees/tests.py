from django.test import TestCase
from employees.models import Employee


class empemployeeTest(TestCase):
    # cria um funcionario padrão
    def setUp(self):
        Employee.objects.create(
            name='carlos', email='teste@gmail.com', department='NOC')
        Employee.objects.create(
            name='vinicius', email='vinie@gmail.com', department='help-desk')

    def test_employee_info(info):
        print('testing Employee Information')
        funcionarioOne = Employee.objects.get(
            name='carlos', email='teste@gmail.com', department='NOC')
        funcionarioTwo = Employee.objects.get(
            name='vinicius', email='vinie@gmail.com', department='help-desk')

