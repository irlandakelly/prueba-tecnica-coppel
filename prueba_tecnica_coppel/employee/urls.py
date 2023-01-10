from django.urls import path
from employee import views
from employee.views import RegistrarEmpleado, ModificarEmpleado, BajaEmpleado

urlpatterns = [
    path('registrar', RegistrarEmpleado.as_view()),
    path('modificar', ModificarEmpleado.as_view()),
    path('baja', BajaEmpleado.as_view()),
    path('detalle', views.detalle_empleados),
]
