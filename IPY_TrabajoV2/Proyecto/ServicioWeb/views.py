from decimal import Context
from django.http import response
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .form import ConductorForm, VehiculoForm, DespachoForm, VentaForm
from django.views.generic import ListView
from Crud.models import Conductor,Venta,Despacho


# Create your views here.
def index(request):
    args = {}
    texto = 'index'
    args['titulo'] = texto
    return render(request, "index.html", args)

def localizacion(request):
    context = {'titulo': 'Localizacion'}
    return render(request, "web/localizacion.html", context)

def despacho(request):
    despacho = requests.get('http://127.0.0.1:8000/gestion/despacho/').json()
    context = {'despacho':despacho,'titulo': 'Despacho'}
    return render(request, "web/despacho.html", context)

# Listar


def lista_general(request):
    conductor = requests.get('http://127.0.0.1:8000/administracion/api/conductor/').json()
    vehiculo = requests.get('http://127.0.0.1:8000/administracion/api/vehiculo/').json()
    context = {'conductor': conductor,'vehiculo': vehiculo, 'titulo': 'Conductor'}
    return render(request, "web/lista.html", context)


@login_required
def venta_lista(request):
    venta = requests.get('http://127.0.0.1:8000/gestion/venta/').json()
    context = {'venta': venta, 'titulo': 'Ventas'}
    return render(request, 'web/venta.html', context)

# Crear


def crear_conductor(request, pk):
    datos = {'form': ConductorForm()}
    if request.method == 'POST':
        form = ConductorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            datos['mensaje'] = 'Guardados correctamente'
            return render(request, 'web/conductor_form.html', datos)
    else:
        form = ConductorForm()
    context = {'form': form, 'datos': datos, 'titulo': 'Conductor'}
    return render(request, 'web/conductor_form.html', context)


def crear_vehiculo(request):
    datos = {'form': VehiculoForm()}
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            datos['mensaje'] = 'Guardados correctamente'
            return render(request, 'web/vehiculo_form.html', datos)
    else:
        form = VehiculoForm()
    context = {'form': form, 'datos': datos}
    return render(request, 'web/vehiculo_form.html', context)

def crear_despacho(request):
    datos = {'form': DespachoForm}
    if request.method == 'POST':
        form = DespachoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            datos['mensaje'] = 'Despacho Guardado Correctamente'
    else:
        form = DespachoForm()
    context = {'form': form, 'datos': datos, 'titulo': 'Despacho'}
    return render(request, 'web/despacho_form.html', context)

# Actualizar

def actualizar_venta(request, pk):
    venta = Venta.objects.get(id=pk)
    info = {'form': VentaForm(instance=venta)}
    if request.method == 'POST':
        info = VentaForm(data=request.POST, instance=venta)
        if info.is_valid():
            info.save()
            info['mensaje'] = 'Guardado Correctamente'
    return render(request,'web/despacho_form.html',info)

def actualizar_conductor(request,pk):
    conductor = Conductor.objects.get(id=pk)
    datos = {'form':ConductorForm(instance=conductor)}
    if request.method == 'POST':
        formulario = ConductorForm(data=request.POST, instance=conductor)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Conductor Actualizado'
    return render(request,'web/update_conductor.html', datos)

# Eliminar

def eliminar_conductor(request,pk):
    conductor = Conductor.objects.get(id=pk)
    conductor.delete()
    conductor = requests.get('http://127.0.0.1:8000/administracion/api/conductor/').json()
    vehiculo = requests.get('http://127.0.0.1:8000/administracion/api/vehiculo/').json()
    context = {'conductor':conductor,'vehiculo':vehiculo}
    return render(request,"web/lista.html",context)

def loginpage(request):
	if request.user.is_authenticated:
		return redirect(index,{'titulo':'Login'})
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect(index,{'titulo':'Login'})
			else:
				messages.info(request, 'Usuario y/o contraseña incorrecto')
		return render(request, "web/login.html", {'titulo':'Login'})
