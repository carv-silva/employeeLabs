from django.contrib import admin
from django.urls import path, include
from employees.views import EmployeesViewSet, DepartmentsViewSet, PayrollsViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'employees', EmployeesViewSet)
router.register(r'departments', DepartmentsViewSet)
router.register(r'payrolls', PayrollsViewSet)
# router.register(r'payrolls', PayrollsListView.as_view())
# path('publishers/', PublisherListView.as_view()),


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
