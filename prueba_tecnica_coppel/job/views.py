from django.shortcuts import render
from job.models import TbCatPuestosPrueba
from job.serializers import PuestoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from datetime import datetime

# Create your views here.
class RegistrarPuesto(APIView):
    def post(self, request):
        data = request.data
        serializer = PuestoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Estatus':'1', 'Mensaje':'Puesto agregado correctamente.'})
        else:
            return Response({'Estatus':'-1', 'Mensaje':'No se agregó el puesto solicitado.'})

class ModificarPuesto(APIView):
    permission_classes = (AllowAny,)
    def put(self, request):
        data = request.data
        try:
            puesto_id = data["id_puesto"]
            puesto_obj = TbCatPuestosPrueba.objects.get(pk=puesto_id)
            serializer = PuestoSerializer(instance=puesto_obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'Estatus':'1', 'Mensaje':'Puesto modificado exitosamente.'})
            else: 
                return Response({'Estatus':'-1', 'Mensaje':'No se modificó el puesto solicitado.'})
        except: 
            return Response({'Estatus':'-1', 'Mensaje':'No se modificó el puesto solicitado.'})


class BajaPuesto(APIView):
    permission_classes = (AllowAny,)
    def put(self, request):
        data = request.data
        try:
            puesto_id = data["id_puesto"]
            puesto_obj = TbCatPuestosPrueba.objects.get(pk=puesto_id)
            serializer = PuestoSerializer(instance=puesto_obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save(estatus=0, fecha_baja=datetime.now().date())
                return Response({'Estatus':'1', 'Mensaje':'Puesto dado de baja correctamente.'})
            else: 
                return Response({'Estatus':'-1', 'Mensaje':'Error.'})
        except: 
            return Response({'Estatus':'-1', 'Mensaje':'No se dió de baja el puesto solicitado.'})


class DetallePuestos(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        puesto_list = TbCatPuestosPrueba.objects.all()
        serializer = PuestoSerializer(puesto_list, many=True)
        return Response(serializer.data)