from django.http import response
from django.shortcuts import render, redirect
from django.urls import reverse
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from .form import ConductorForm, VehiculoForm, DespachoForm, VentaForm,DireccionForm
from Crud.models import Conductor,Venta,Postventa,Despacho,Direccion

# Create your views here.
def index(request):
    args = {}
    texto = 'index'
    args['titulo'] = texto
    return render(request, "index.html", args)

# Mostrar

def viewlocalizacion(request,pk):
    direccion = Direccion.objects.get(id = pk)
    context = {
        'direccion':direccion,
        'token':'pk.eyJ1IjoiYnJheWFubG1sIiwiYSI6ImNrcXNyOWl1YTA1YzQydXNiNXlwdWZsb2UifQ.pA4JkLi_o-OsuuG6ePvPdw',
        'titulo': 'Localizacion'
        }
    return render(request,'web/view_localizacion.html',context)

# Listar

def localizacion(request):
    direccion = Direccion.objects.all()
    context = {
        'direccion':direccion,
        'titulo': 'Localizacion',
    }
    return render(request, 'web/localizacion.html', context)

def postventa_lista(request):
    postventa = requests.get('http://127.0.0.1:8000/gestion/postventa/').json()
    context = {'postventa':postventa,'titulo':'Postventa'}
    return render(request,"web/postventa.html",context)

def despacho(request):
    despacho = requests.get('http://127.0.0.1:8000/gestion/despacho/').json()
    context = {'despacho':despacho,'titulo': 'Despacho'}
    return render(request, "web/despacho.html", context)   

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

def crear_conductor(request):
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

def procesar(request,pk):
    idventa = pk
    venta = Venta.objects.get(id=idventa)
    initial_compra = {
        'estado_compra' : 3
    }
    initial_data = {
        'venta': idventa
    }
    if request.method == 'POST':
        form1 = DespachoForm(request.POST, prefix="form1")
        form2 = VentaForm(request.POST, instance=venta, prefix="form2")
        if form1.is_valid() or form2.is_valid():
            form1.save()
            form2.save()
            return redirect('ServicioWeb:despacho')
    else:
        form1 = DespachoForm(initial=initial_data, prefix="form1")
        form2 = VentaForm(instance=venta, prefix="form2", initial=initial_compra)
    context = {'form1':form1,'form2':form2, 'idventa':idventa}
    return render(request, 'web/procesar.html', context)

def creardireccion(request,pk):
    despacho = Despacho.objects.get(id = pk)
    ventaid = str(despacho.venta)
    conductorid = str(despacho.conductor)
    venta = Venta.objects.get(id = ventaid)
    conductor = Conductor.objects.get(rut = conductorid)
    direccion = str(venta.direccion)
    initial_direccion = {
        'direccion':direccion
    }
    form = DireccionForm(request.POST,prefix = "form")
    if form.is_valid(): 
        form.save()
        return redirect('ServicioWeb:localizacion')
    else:
        form = DireccionForm(initial=initial_direccion, prefix="form")
    context = {'form':form, 'direccion': direccion, 'venta':venta, 'conductor':conductor}
    return render(request,'web/prueba.html', context)

# Actualizar

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
    return redirect('ServicioWeb:lista_general')

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
