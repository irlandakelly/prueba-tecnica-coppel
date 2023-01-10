from django.shortcuts import render, get_object_or_404
from employee.models import TbCatEmpleadosPrueba
from employee.serializers import EmpleadoSerializer, ModificarEmpleadoSerializer, BajaEmpleadoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

# Create your views here.


class RegistrarEmpleado(APIView):
    def post(self, request):
        data = request.data
        serializer = EmpleadoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Estatus':'1', 'Mensaje':'Empleado registrado exitosamente.'})


class ModificarEmpleado(APIView):
    permission_classes = (AllowAny,)
    def put(self, request):
        data = request.data
        empleado_id = data["num_empleado"]
        empleado_obj = TbCatEmpleadosPrueba.objects.get(pk=empleado_id)
        serializer = EmpleadoSerializer(instance=empleado_obj, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Estatus':'1', 'Mensaje':'Empleado modificado exitosamente.'})


class BajaEmpleado(APIView):
    def put(self, request):
        data = request.data
        serializer = BajaEmpleadoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Estatus':'1', 'Mensaje':'Empleado modificado exitosamente.'})