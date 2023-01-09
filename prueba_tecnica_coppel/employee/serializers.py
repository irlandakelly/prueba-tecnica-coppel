from rest_framework import serializers
from employee.models import TbCatEmpleadosPrueba, TbCatPuestosPrueba

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCatEmpleadosPrueba
        fields = '__all__'

class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCatPuestosPrueba
        fields = '__all__'