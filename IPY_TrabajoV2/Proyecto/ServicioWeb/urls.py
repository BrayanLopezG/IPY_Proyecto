from django.urls import path,include
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.resolvers import URLPattern
from . import views

app_name='ServicioWeb'

urlpatterns = [
    path('', views.index, name="index"),
    path('conductor/', views.conductor_lista, name="lista"),
    path('despacho/', views.despacho, name="despacho"),
    path('venta/', views.venta, name= "venta"),
    path('localizacion/', views.localizacion, name="localizacion"),
    path('login/', LoginView.as_view(template_name = 'web/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name = 'web/index.html'), name='logout'),
]
   
