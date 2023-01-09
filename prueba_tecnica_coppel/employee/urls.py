from django.urls import path
from employee.views import RegistrarEmpleado

urlpatterns = [
    path('registrar', RegistrarEmpleado.as_view())
]
