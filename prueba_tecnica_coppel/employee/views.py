from django.shortcuts import render, redirect
from employee.models import TbCatEmpleadosPrueba
from django import forms
from employee.forms import EmpleadoForm, BajaEmpleadoForm
from job.models import TbCatPuestosPrueba
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def registrar_empleado(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                num_empleado = form.cleaned_data['num_empleado']
                messages.info(request, 'Estatus = 1')
                messages.info(request, 'Empleado ' + str(num_empleado) + ' registrado exitosamente.')
                return HttpResponseRedirect(reverse('detalle_empleado', args=[num_empleado]))
            except:
                pass
        else:
            messages.info(request, 'Estatus = -1')
            messages.info(request, 'Empleado ya se encuentra registrado.')
    else:
        form = EmpleadoForm()   
    return render(request, 'registrar.html', {'form':form})


def modificar_empleado(request, id):
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
            messages.info(request, 'Estatus = -1')
            messages.info(request, 'No se modificó información.')
    else:
        form = EmpleadoForm()
    context = {'empleado':empleado, 'form':form, 'puestos':puestos}
    return render(request, 'modificar.html', context)


def baja_empleado(request, id):
    empleado = TbCatEmpleadosPrueba.objects.get(num_empleado=id)
    date = datetime.now().date()
    empleado.fecha_baja = date
    empleado.estatus = 0
    
    print(date)
    if request.method == "POST":
        form = BajaEmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            try:
                form.save()
                num_empleado = form.cleaned_data['num_empleado']
                messages.info(request, 'Estatus = 1')
                messages.info(request, 'Empleado ' + str(num_empleado) + ' dado de baja correctamente.')
                return HttpResponseRedirect(reverse('detalle_empleado', args=[num_empleado]))
            except: 
                pass
        else:
            print(form.errors)
            messages.info(request, 'Estatus = -1')
            messages.info(request, 'No se pudo dar de baja.')
    else:
        form = EmpleadoForm()
    
    context = {'empleado':empleado, 'form':form}
    return render(request, 'baja.html', context)


def detalle_empleados(request):
    empleados = TbCatEmpleadosPrueba.objects.all()
    return render(request,"detalles.html",{'empleados':empleados})


def detalle_empleado(request, id):
    empleado = TbCatEmpleadosPrueba.objects.filter(num_empleado=id)
    return render(request,"detalles.html",{'empleados':empleado})