from django.http import request
from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm

def home(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos' : vehiculos
    }
    return render(request, 'app/home.html', datos)    
def form_vehiculo(request):
    datos = {
        'form' : VehiculoForm()
    }
    if request.method =='POST':
        formulario = VehiculoForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados Correctamente"

    return render(request, 'app/form_vehiculo.html', datos)

def form_mod_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)

    datos = {
        'form' : VehiculoForm(instance=vehiculo)
    }
    if request.method=='POST':
        formulario = VehiculoForm(data=request.POST, instance=vehiculo)

        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificados Correctamente"

    return render(request, 'app/form_mod_vehiculo.html', datos)

def modificar_vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    datos = {
        'vehiculos' : vehiculos
    }
    return render(request, 'app/modificar_vehiculo.html', datos)

def form_del_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    vehiculo.delete()

    return redirect(to="modificar_vehiculo")