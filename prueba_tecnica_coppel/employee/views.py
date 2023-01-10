from django.shortcuts import render, redirect
from employee.models import TbCatEmpleadosPrueba
from employee.serializers import EmpleadoSerializer
from employee.forms import EmpleadoForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from datetime import datetime

# Create your views here.


class RegistrarEmpleado(APIView):
    def post(self, request):
        data = request.data
        serializer = EmpleadoSerializer(data=data)
        empleado_id = data["num_empleado"]
        if serializer.is_valid():
            serializer.save()
            return Response({'Estatus':'1', 'Mensaje':'Empleado ' + str(empleado_id) + ' registrado exitosamente.', 'Datos':serializer.data})
        else: 
            return Response({'Estatus':'-1', 'Mensaje':'Empleado ' + str(empleado_id) + ' ya se encuentra registrado.'})


class ModificarEmpleado(APIView):
    permission_classes = (AllowAny,)
    def put(self, request):
        data = request.data
        try:
            empleado_id = data["num_empleado"]
            empleado_obj = TbCatEmpleadosPrueba.objects.get(pk=empleado_id)
            serializer = EmpleadoSerializer(instance=empleado_obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Estatus':'1', 'Mensaje':'Empleado ' + str(empleado_id) + ' modificado exitosamente.'})
            else: 
                return Response({'Estatus':'-1', 'Mensaje':'Empleado ' + str(empleado_id) + ' no se modificó información.'})
        except: 
            return Response({'Estatus':'-1', 'Mensaje':'Empleado ' + str(empleado_id) + ' no se modificó información.'})
        


class BajaEmpleado(APIView):
    permission_classes = (AllowAny,)
    def put(self, request):
        data = request.data
        try:
            empleado_id = data["num_empleado"]
            empleado_obj = TbCatEmpleadosPrueba.objects.get(pk=empleado_id)
            serializer = EmpleadoSerializer(instance=empleado_obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(estatus=0, fecha_baja=datetime.now().date())
                return Response({'Estatus':'1', 'Mensaje':'Empleado ' + str(empleado_id) + ' dado de baja exitosamente.'})
            else: 
                return Response({'Estatus':'-1', 'Mensaje':'Error.'})
        except: 
            return Response({'Estatus':'-1', 'Mensaje':'Empleado ' + str(empleado_id) + ' no se pudo dar de baja debido a que no existe.'})



def detalle_empleados(request):
    empleados = TbCatEmpleadosPrueba.objects.all()
    return render(request,"detalles.html",{'empleados':empleados})