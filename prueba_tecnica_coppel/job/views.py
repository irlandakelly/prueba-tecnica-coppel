from django.shortcuts import render
from job.models import TbCatPuestosPrueba
from job.forms import PuestoForm, BajaPuestoForm, MenuPuestoForm, ModificarPuestoForm
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
                return HttpResponseRedirect(reverse('registrar_puesto'))
            elif opcion == '2':
                return HttpResponseRedirect(reverse('modificar_puesto', args=[id_puesto]))
            elif opcion == '3':
                return HttpResponseRedirect(reverse('baja_puesto', args=[id_puesto]))
            elif opcion == '4':
                if id_puesto == '0':
                    messages.success(request, 'Estatus = 1')
                    messages.success(request, 'Puestos encontrados.')
                    return HttpResponseRedirect(reverse('detalle'))
                else: 
                    try:
                        puesto = TbCatPuestosPrueba.objects.get(id_puesto=id_puesto)
                        if puesto.estatus == 0:
                            messages.error(request, 'Estatus = -1')
                            messages.error(request, 'Puesto ' + str(id_puesto) + ' no encontrado.')
                            return HttpResponseRedirect(reverse('menu_puestos'))
                        else:
                            messages.success(request, 'Estatus = 1')
                            messages.success(request, 'Puesto ' + str(id_puesto) + ' encontrado.')
                            return render(request,"detalles_puesto.html",{'puestos':puesto})
                    except:
                        pass
                    return HttpResponseRedirect(reverse('detalle_puesto', args=[id_puesto]))      
    else:
        form = MenuPuestoForm()
    return render(request, 'index_puesto.html', {'form':form})



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
    return render(request, 'registrar_puesto.html', {'form':form})


def modificar_puesto(request, id):
    try:
        puesto = TbCatPuestosPrueba.objects.get(id_puesto=id)
        puestos = TbCatPuestosPrueba.objects.all()
        print(str(id))
        if request.method == "POST":
            form = ModificarPuestoForm(request.POST, instance=puesto)
            if form.is_valid():
                try:
                    form.save()
                    id_puesto = form.cleaned_data['id_puesto']
                    messages.success(request, 'Estatus = 1')
                    messages.success(request, 'Puesto ' + str(id_puesto) + ' modificado exitosamente.')
                    return HttpResponseRedirect(reverse('detalle_puesto', args=[id_puesto]))
                except: 
                    pass
            else:
                print(form.errors)
                messages.error(request, 'Estatus = -1')
                messages.error(request, 'Ocurrió un error.')
        else:
            form = PuestoForm()
        context = {'puesto':puesto, 'form':form, 'puestos':puestos}
        return render(request, 'modificar_puesto.html', context)
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
            print('request bien')
            if form.is_valid():
                try:
                    form.save()
                    id_puesto = form.cleaned_data['id_puesto']
                    messages.success(request, 'Estatus = 1')
                    messages.success(request, 'Puesto ' + str(id_puesto) + ' dado de baja correctamente.')
                    print('y no msg')
                except: 
                    pass
            else:
                messages.error(request, 'Estatus = -1')
                messages.error(request, 'No se pudo dar de baja.')
        else:
            form = PuestoForm()
        
        context = {'puesto':puesto, 'form':form}
        return render(request, 'baja_puesto.html', context)
    except:
        messages.error(request, 'Estatus = -1')
        messages.error(request, 'No se modificó el puesto ' + str(id) + ' porque no existe.')
        return HttpResponseRedirect(reverse('menu_puestos'))


def detalle_puestos(request):
    puestos = TbCatPuestosPrueba.objects.filter(estatus='1')
    return render(request,"detalles_puesto.html",{'puestos':puestos})


def detalle_puesto(request, id):
    try:
        puesto = TbCatPuestosPrueba.objects.filter(id_puesto=id)
        if puesto:
            return render(request,"detalles_puesto.html",{'puestos':puesto})
        else:
            messages.error(request, 'Estatus = -1')
            messages.error(request, 'Puesto ' + str(id) + ' no encontrado.')
        return HttpResponseRedirect(reverse('menu_puestos'))
    except:
        pass

