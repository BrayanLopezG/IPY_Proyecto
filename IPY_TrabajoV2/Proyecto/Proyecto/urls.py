"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework import routers
from Crud import views
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'conductor',views.ConductorViewSet)
router.register(r'vehiculo',views.VehiculoViewSet)
router.register(r'venta',views.VentaViewSet)
router.register(r'postventa',views.PostventaViewSet)
router.register(r'despacho',views.DespachoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gestion/',include('Crud.urls')),
    path('',include('ServicioWeb.urls')), 
    path('administracion/api/', include(router.urls)), 
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
