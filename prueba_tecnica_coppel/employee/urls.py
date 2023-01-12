from django.urls import path
from employee import views

urlpatterns = [
    path('', views.menu, name='menu_principal'),
    path('registrar/', views.registrar_empleado, name='registrar'),
    path('detalle/', views.detalle_empleados, name='detalle'),
    path('detalle/<int:id>/', views.detalle_empleado, name='detalle_empleado'),
    path('modificar/<int:id>/', views.modificar_empleado, name='modificar_empleado'),
    path('baja/', views.baja_empleado, name='baja'),
    path('baja/<int:id>/', views.baja_empleado, name='baja_empleado'),
]
