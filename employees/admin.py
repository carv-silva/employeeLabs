from django.contrib import admin
from django.contrib import admin
from employees.models import Employee


# criacao do admin
class Employees(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


# registro do funcionarios no admin
admin.site.register(Employee, Employees)
