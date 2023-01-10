# Generated by Django 4.1.5 on 2023-01-10 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TbCatEmpleadosPrueba',
            fields=[
                ('keyx', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('ap_paterno', models.CharField(max_length=50)),
                ('ap_materno', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=60)),
                ('cp', models.CharField(max_length=5)),
                ('telefono', models.CharField(max_length=10)),
                ('curp', models.CharField(max_length=18)),
                ('nss', models.CharField(max_length=11)),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('num_empleado', models.IntegerField(unique=True)),
                ('fecha_baja', models.DateField(default='1900-01-01')),
                ('estatus', models.SmallIntegerField(default=1)),
                ('causa_baja', models.CharField(default='', max_length=255)),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.tbcatpuestosprueba')),
            ],
        ),
    ]