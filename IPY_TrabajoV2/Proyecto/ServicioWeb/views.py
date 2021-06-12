from django.http import response
from django.shortcuts import render,redirect
from django.urls import reverse
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "index.html")

def venta(request):
    return render(request, "web/venta.html")

def localizacion(request):
    return render(request, "web/localizacion.html")

def despacho(request):
    return render(request, "web/despacho.html")

def conductor_lista(request):
    conductor = requests.get('http://127.0.0.1:8000/gestion/conductor/').json()
    vehiculo = requests.get('http://127.0.0.1:8000/gestion/vehiculo/').json()
    context = {'conductor':conductor,'vehiculo':vehiculo}
    return render(request,"web/lista.html",context)

'''def ingresar(request):
    conductor = requests.post('http://127.0.0.1:8000/gestion/concrear').json()
    vehiculo = requests.post('http://127.0.0.1:8000/gestion/vehcrear').json()
    return render(request,
        'web/index.html',
        {'conductor':conductor,
         'vehiculo':vehiculo,}
    )'''

def loginpage(request):
	if request.user.is_authenticated:
		return redirect(index)
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect(index)
			else:
				messages.info(request, 'Usuario y/o contraseña incorrecto')
		context = {}
		return render(request, "web/login.html", context)