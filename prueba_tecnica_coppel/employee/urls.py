from django.urls import path
from employee import views
from employee.views import ModificarEmpleado, BajaEmpleado

urlpatterns = [
    path('modificar', ModificarEmpleado.as_view()),
    path('baja', BajaEmpleado.as_view()),
    path('registrar/', views.registrar_empleado),
    path('detalle/', views.detalle_empleados),
    path('detalle/<int:id>/', views.detalle_empleado, name='detalle_empleado'),
]
