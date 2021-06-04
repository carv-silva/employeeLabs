from django.contrib import admin
from django.contrib import admin
from employees.models import Employee, Department, Payroll


class Departments(admin.ModelAdmin):
    list_display = ('id', 'name', 'budget', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')


# registro do Departamento no admin
admin.site.register(Department, Departments)


class Employees(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'startDate',
                    'terminationDate', 'department')
    list_display_links = ('id', 'name')
    # search_fields = ('nameEmployee', 'nameDepartment')


# registro do funcionarios no admin
admin.site.register(Employee, Employees)


class Payrolls(admin.ModelAdmin):
    list_display = ('id', 'month', 'employee',
                    'gross_salary', 'taxes', 'benefits', 'net_salary')
    list_display_links = ('id',)
    search_fields = ('name', 'description')


admin.site.register(Payroll, Payrolls)









