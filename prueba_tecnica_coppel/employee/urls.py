from django.urls import path
from employee.views import RegistrarEmpleado, ModificarEmpleado, BajaEmpleado, DetalleEmpleados

urlpatterns = [
    path('registrar', RegistrarEmpleado.as_view()),
    path('modificar', ModificarEmpleado.as_view()),
    path('baja', BajaEmpleado.as_view()),
    path('detalle', DetalleEmpleados.as_view()),
]
