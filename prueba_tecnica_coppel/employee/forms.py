from django import forms  
from employee.models import TbCatEmpleadosPrueba


class EmpleadoForm(forms.ModelForm):  
    class Meta:  
        model = TbCatEmpleadosPrueba 
        fields = "__all__"  