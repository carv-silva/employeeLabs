from django.db.models.base import Model
from rest_framework import serializers
from employees.models import Employee


# serializador de modelo
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'department']

