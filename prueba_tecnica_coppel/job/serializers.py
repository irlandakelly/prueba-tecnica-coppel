from rest_framework import serializers
from job.models import TbCatPuestosPrueba

class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TbCatPuestosPrueba
        fields = '__all__'