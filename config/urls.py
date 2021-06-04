from django.contrib import admin
from django.urls import path, include
from employees.views import EmployeesViewSet, DepartmentsViewSet, PayrollsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employee', EmployeesViewSet)
router.register(r'departments', DepartmentsViewSet)
router.register(r'payrolls', PayrollsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
