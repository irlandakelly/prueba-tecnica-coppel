from rest_framework import serializers
from employee.models import TbCatEmpleadosPrueba

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCatEmpleadosPrueba
        fields = '__all__'
