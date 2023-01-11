from django import forms
from employee.models import TbCatEmpleadosPrueba
from job.models import TbCatPuestosPrueba


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