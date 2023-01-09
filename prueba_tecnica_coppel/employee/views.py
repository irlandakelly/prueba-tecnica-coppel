from django.shortcuts import render
from employee.models import TbCatEmpleadosPrueba
from employee.serializers import EmpleadoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RegistrarEmpleado(APIView):
    def post(self, request):
        data = request.data
        serializer = EmpleadoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Estatus':'1', 'Mensaje':'Empleado registrado exitosamente.'})


