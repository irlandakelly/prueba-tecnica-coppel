from django.db import models

# Create your models here.
class TbCatPuestosPrueba(models.Model):
    keyx = models.AutoField(primary_key=True)
    fecha_alta = models.DateField(auto_now_add=True)
    id_puesto = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=100, unique=True)
    estatus = models.SmallIntegerField(default=1)
    fecha_baja = models.DateField(default='1900-01-01')
    empleado_registra = models.IntegerField(null=False)
    empleado_baja = models.IntegerField(blank=True, null=True)