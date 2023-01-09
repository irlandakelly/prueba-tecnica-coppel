from django.shortcuts import render
from job.models import TbCatPuestosPrueba
from job.serializers import PuestoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class RegistrarPuesto(APIView):
    def post(self, request):
        data = request.data
        serializer = PuestoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Estatus':'1', 'Mensaje':'Puesto agregado correctamente.'})