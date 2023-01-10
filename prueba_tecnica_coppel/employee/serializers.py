from rest_framework import serializers
from employee.models import TbCatEmpleadosPrueba
import datetime

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCatEmpleadosPrueba
        fields = '__all__'

class ModificarEmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCatEmpleadosPrueba
        fields = ('num_empleado', 'direccion', 'cp', 'telefono', 'curp', 'nss', 'puesto')

class BajaEmpleadoSerializer(serializers.ModelSerializer):
    fecha_baja = datetime.date.today()
    class Meta:
        model = TbCatEmpleadosPrueba
        fields = ('num_empleado', 'estatus', 'fecha_baja','causa_baja')