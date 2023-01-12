from django.shortcuts import render
from job.models import TbCatPuestosPrueba
from job.forms import PuestoForm, BajaPuestoForm, MenuPuestoForm
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


# Create your views here.

def menu(request):
    if request.method == "POST":
        form = MenuPuestoForm(request.POST)
        if form.is_valid():
            id_puesto = request.POST.get('id_puesto')
            opcion = request.POST.get('menu_principal')
            if opcion == '1':
                return HttpResponseRedirect(reverse('registrar'))
            elif opcion == '2':
                return HttpResponseRedirect(reverse('modificar_puesto', args=[id_puesto]))
            elif opcion == '3':
                return HttpResponseRedirect(reverse('baja_puesto', args=[id_puesto]))
            elif opcion == '4':
                if id_puesto == '0':
                    messages.info(request, 'Estatus = 1')
                    messages.info(request, 'Puestos encontrados.')
                    return HttpResponseRedirect(reverse('detalle'))
                else:
                    return HttpResponseRedirect(reverse('detalle_puesto', args=[id_puesto]))      
    else:
        form = MenuPuestoForm()
    return render(request, 'index.html', {'form':form})



def registrar_puesto(request):
    if request.method == "POST":
        form = PuestoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                id_puesto = form.cleaned_data['id_puesto']
                messages.success(request, 'Estatus = 1')
                messages.success(request, 'Puesto ' + str(id_puesto) + ' registrado exitosamente.')
                return HttpResponseRedirect(reverse('detalle_puesto', args=[id_puesto]))
            except:
                pass
        else:
            messages.error(request, 'Estatus = -1')
            messages.error(request, 'Puesto ya se encuentra registrado.')
    else:
        form = PuestoForm()   
    return render(request, 'registrar.html', {'form':form})


def modificar_puesto(request, id):
    try:
        puesto = TbCatPuestosPrueba.objects.get(id_puesto=id)
        puestos = TbCatPuestosPrueba.objects.all()
        if request.method == "POST":
            form = PuestoForm(request.POST, instance=puesto)
            if form.is_valid():
                try:
                    form.save()
                    id_puesto = form.cleaned_data['id_puesto']
                    messages.info(request, 'Estatus = 1')
                    messages.info(request, 'Puesto ' + str(id_puesto) + ' modificado exitosamente.')
                    return HttpResponseRedirect(reverse('detalle_puesto', args=[id_puesto]))
                except: 
                    pass
            else:
                messages.error(request, 'Estatus = -1 \n No se modificó información.')
                messages.error(request, 'Puesto ' + str(id) + ' No se modificó información.')
        else:
            form = PuestoForm()
        context = {'puesto':puesto, 'form':form, 'puestos':puestos}
        return render(request, 'modificar.html', context)
    except:
        messages.error(request, 'Estatus = -1')
        messages.error(request, 'Puesto ' + str(id) + ' no se modificó información.')
        return HttpResponseRedirect(reverse('menu_principal'))
        
def baja_puesto(request, id):
    try:
        puesto = TbCatPuestosPrueba.objects.get(id_puesto=id)
        date = datetime.now().date()
        puesto.fecha_baja = date
        puesto.estatus = 0

        if request.method == "POST":
            form = BajaPuestoForm(request.POST, instance=puesto)
            if form.is_valid():
                try:
                    form.save()
                    id_puesto = form.cleaned_data['id_puesto']
                    messages.info(request, 'Estatus = 1')
                    messages.info(request, 'puesto ' + str(id_puesto) + ' dado de baja correctamente.')
                    
                except: 
                    pass
            else:
                messages.error(request, 'Estatus = -1')
                messages.error(request, 'No se pudo dar de baja.')
        else:
            form = PuestoForm()
        
        context = {'puesto':puesto, 'form':form}
        return render(request, 'baja.html', context)
    except:
        messages.error(request, 'Estatus = -1')
        messages.error(request, 'No se modificó el puesto ' + str(id) + ' porque no existe.')
        return HttpResponseRedirect(reverse('menu_principal'))


def detalle_puestos(request):
    puestos = TbCatPuestosPrueba.objects.filter(estatus='1')
    return render(request,"detalles.html",{'puestos':puestos})


def detalle_puesto(request, id):
    try:
        puesto = TbCatPuestosPrueba.objects.filter(id_puesto=id)
        singular = TbCatPuestosPrueba.objects.get(id_puesto=id)

        if singular.estatus == 0:
            messages.error(request, 'Estatus = -1')
            messages.error(request, 'Puesto ' + str(id) + ' no encontrado.')
            return HttpResponseRedirect(reverse('menu_principal'))
        else:
            messages.info(request, 'Estatus = 1')
            messages.info(request, 'Puesto ' + str(id) + ' encontrado.')
            return render(request,"detalles.html",{'puestos':puesto})
    except:
        messages.error(request, 'Estatus = -1')
        messages.error(request, 'Puesto ' + str(id) + ' no encontrado.')
        return HttpResponseRedirect(reverse('menu_principal'))

