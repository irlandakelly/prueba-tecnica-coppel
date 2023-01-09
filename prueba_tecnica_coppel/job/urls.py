from django.urls import path
from job.views import RegistrarPuesto

urlpatterns = [
    path('registrar', RegistrarPuesto.as_view())
]