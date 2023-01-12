from django.urls import path
from job import views

urlpatterns = [
    path('', views.menu, name='menu_puestos'),
    path('registrar/', views.registrar_puesto, name='registrar_puesto'),
    path('detalle/', views.detalle_puestos, name='detalle'),
    path('detalle/<int:id>/', views.detalle_puesto, name='detalle_puesto'),
    path('modificar/<int:id>/', views.modificar_puesto, name='modificar_puesto'),
    path('baja/', views.baja_puesto, name='baja'),
    path('baja/<int:id>/', views.baja_puesto, name='baja_puesto'),
]
