from django.urls import path
from employee import views

urlpatterns = [
    path('registrar/', views.registrar_empleado),
    path('detalle/', views.detalle_empleados),
    path('detalle/<int:id>/', views.detalle_empleado, name='detalle_empleado'),
    path('modificar/<int:id>/', views.modificar_empleado, name='modificar_empleado'),
    path('baja/', views.modificar_empleado, name='modificar_empleado'),
    path('baja/<int:id>/', views.baja_empleado, name='baja_empleado'),
]
