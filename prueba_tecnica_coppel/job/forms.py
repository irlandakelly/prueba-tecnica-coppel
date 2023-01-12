from django import forms
from employee.models import TbCatEmpleadosPrueba
from job.models import TbCatPuestosPrueba


class PuestoForm(forms.ModelForm):
    class Meta:
        model = TbCatPuestosPrueba
        fields = [
            'id_puesto', 'descripcion', 'empleado_registra'
        ]

class ModificarPuestoForm(forms.ModelForm):
    class Meta:
        model = TbCatPuestosPrueba
        fields = [
            'id_puesto', 'descripcion'
        ]

class BajaPuestoForm(forms.ModelForm):
    class Meta:
        model = TbCatPuestosPrueba
        fields = [
            'id_puesto', 'empleado_baja', 'fecha_baja', 'estatus'
        ]

menu_opcion = (
    ("1", "Registrar"),
    ("2", "Modificar"),
    ("3", "Dar de baja"),
    ("4", "Consultar")
)

class MenuPuestoForm(forms.Form):
    class Meta:
        id_puesto = forms.IntegerField()
        opcion = forms.ChoiceField(choices=menu_opcion)