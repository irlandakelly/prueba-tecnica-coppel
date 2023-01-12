from django import forms
from employee.models import TbCatEmpleadosPrueba
from job.models import TbCatPuestosPrueba
from datetime import datetime


class EmpleadoForm(forms.ModelForm):
    puesto = forms.ModelChoiceField(queryset=TbCatPuestosPrueba.objects.all(),
                                    to_field_name = 'descripcion',
                                    empty_label="Seleccione Puesto")
    class Meta:
        model = TbCatEmpleadosPrueba
        fields = [
            'num_empleado', 'nombre', 'ap_paterno', 'ap_materno', 'direccion', 'cp',
            'telefono', 'curp', 'nss', 'puesto',
        ]

class BajaEmpleadoForm(forms.ModelForm):
    class Meta:
        model = TbCatEmpleadosPrueba
        fields = [
            'num_empleado', 'causa_baja', 'fecha_baja', 'estatus'
        ]

menu_opcion = (
    ("1", "Registrar"),
    ("2", "Modificar"),
    ("3", "Dar de baja"),
    ("4", "Consultar")
)

class MenuEmpleadoForm(forms.Form):
    class Meta:
        num_empleado = forms.IntegerField()
        opcion = forms.ChoiceField(choices=menu_opcion)