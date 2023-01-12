from django.shortcuts import render
from employee.models import TbCatEmpleadosPrueba
from employee.forms import EmpleadoForm, BajaEmpleadoForm, MenuEmpleadoForm
from job.models import TbCatPuestosPrueba
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.

def menu(request):
    if request.method == "POST":
        form = MenuEmpleadoForm(request.POST)
        if form.is_valid():
            num_empleado = request.POST.get('num_empleado')
            opcion = request.POST.get('menu_principal')
            if opcion == '1':
                return HttpResponseRedirect(reverse('registrar'))
            elif opcion == '2':
                return HttpResponseRedirect(reverse('modificar_empleado', args=[num_empleado]))
            elif opcion == '3':
                return HttpResponseRedirect(reverse('baja_empleado', args=[num_empleado]))
            elif opcion == '4':
                if num_empleado == '0':
                    messages.info(request, 'Estatus = 1')
                    messages.info(request, 'Empleados encontrados.')
                    return HttpResponseRedirect(reverse('detalle'))
                else:
                    return HttpResponseRedirect(reverse('detalle_empleado', args=[num_empleado]))      
    else:
        form = MenuEmpleadoForm()
    return render(request, 'index.html', {'form':form})



def registrar_empleado(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                num_empleado = form.cleaned_data['num_empleado']
                messages.success(request, 'Estatus = 1')
                messages.success(request, 'Empleado ' + str(num_empleado) + ' registrado exitosamente.')
                return HttpResponseRedirect(reverse('detalle_empleado', args=[num_empleado]))
            except:
                pass
        else:
            messages.error(request, 'Estatus = -1')
            messages.error(request, 'Empleado ya se encuentra registrado.')
    else:
        form = EmpleadoForm()   
    return render(request, 'registrar.html', {'form':form})


def modificar_empleado(request, id):
    try:
        empleado = TbCatEmpleadosPrueba.objects.get(num_empleado=id)
        puestos = TbCatPuestosPrueba.objects.all()
        if request.method == "POST":
            form = EmpleadoForm(request.POST, instance=empleado)
            if form.is_valid():
                try:
                    form.save()
                    num_empleado = form.cleaned_data['num_empleado']
                    messages.info(request, 'Estatus = 1')
                    messages.info(request, 'Empleado ' + str(num_empleado) + ' modificado exitosamente.')
                    return HttpResponseRedirect(reverse('detalle_empleado', args=[num_empleado]))
                except: 
                    pass
            else:
                messages.error(request, 'Estatus = -1 \n No se modificó información.')
                messages.error(request, 'Empleado ' + str(id) + ' No se modificó información.')
        else:
            form = EmpleadoForm()
        context = {'empleado':empleado, 'form':form, 'puestos':puestos}
        return render(request, 'modificar.html', context)
    except:
        messages.error(request, 'Estatus = -1')
        messages.error(request, 'Empleado ' + str(id) + ' no se modificó información.')
        return HttpResponseRedirect(reverse('menu_principal'))
        
def baja_empleado(request, id):
    try:
        empleado = TbCatEmpleadosPrueba.objects.get(num_empleado=id)
        date = datetime.now().date()
        empleado.fecha_baja = date
        empleado.estatus = 0

        if request.method == "POST":
            form = BajaEmpleadoForm(request.POST, instance=empleado)
            if form.is_valid():
                try:
                    form.save()
                    num_empleado = form.cleaned_data['num_empleado']
                    messages.info(request, 'Estatus = 1')
                    messages.info(request, 'Empleado ' + str(num_empleado) + ' dado de baja correctamente.')
                    
                except: 
                    pass
            else:
                messages.error(request, 'Estatus = -1')
                messages.error(request, 'No se pudo dar de baja.')
        else:
            form = EmpleadoForm()
        
        context = {'empleado':empleado, 'form':form}
        return render(request, 'baja.html', context)
    except:
        messages.error(request, 'Estatus = -1')
        messages.error(request, 'No se modificó el empleado ' + str(id) + ' porque no existe.')
        return HttpResponseRedirect(reverse('menu_principal'))


def detalle_empleados(request):
    empleados = TbCatEmpleadosPrueba.objects.filter(estatus='1')
    return render(request,"detalles.html",{'empleados':empleados})


def detalle_empleado(request, id):
    try:
        empleado = TbCatEmpleadosPrueba.objects.filter(num_empleado=id)
        singular = TbCatEmpleadosPrueba.objects.get(num_empleado=id)

        if singular.estatus == 0:
            messages.error(request, 'Estatus = -1')
            messages.error(request, 'Empleado ' + str(id) + ' no encontrado.')
            return HttpResponseRedirect(reverse('menu_principal'))
        else:
            messages.info(request, 'Estatus = 1')
            messages.info(request, 'Empleado ' + str(id) + ' encontrado.')
            return render(request,"detalles.html",{'empleados':empleado})
    except:
        messages.error(request, 'Estatus = -1')
        messages.error(request, 'Empleado ' + str(id) + ' no encontrado.')
        return HttpResponseRedirect(reverse('menu_principal'))

