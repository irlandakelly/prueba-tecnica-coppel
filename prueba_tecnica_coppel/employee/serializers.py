from rest_framework import serializers
from employee.models import TbCatEmpleadosPrueba
import datetime

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCatEmpleadosPrueba
        fields = '__all__'
