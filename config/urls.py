from django.contrib import admin
from django.urls import path, include
from employees.views import EmployeesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employee', EmployeesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
