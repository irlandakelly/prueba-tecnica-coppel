from django.db import models


# Create your models here.
class TbCatEmpleadosPrueba(models.Model):
    keyx = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    direccion = models.CharField(max_length=60)
    cp = models.CharField(max_length=5)
    telefono = models.CharField(max_length=10)
    curp = models.CharField(max_length=18)
    nss = models.CharField(max_length=11)
    fecha_alta = models.DateField(auto_now_add=True)
    num_empleado = models.IntegerField(unique=True)
    puesto = models.ForeignKey('job.TbCatPuestosPrueba', on_delete=models.CASCADE)
    fecha_baja = models.DateField(default='1900-01-01')
    estatus = models.SmallIntegerField(default=1)
    causa_baja = models.CharField(max_length=255, default='')




