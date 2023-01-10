from django.urls import path
from job.views import RegistrarPuesto, ModificarPuesto, BajaPuesto, DetallePuestos

urlpatterns = [
    path('registrar', RegistrarPuesto.as_view()),
    path('modificar', ModificarPuesto.as_view()),
    path('baja', BajaPuesto.as_view()),
    path('detalle', DetallePuestos.as_view()),
]