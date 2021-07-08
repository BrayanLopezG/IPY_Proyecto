from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.resolvers import URLPattern
from . import views

app_name='ServicioWeb'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('localizacion/', views.localizacion, name = 'localizacion'),
    path('login/', LoginView.as_view(template_name = 'web/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'web/index.html'), name = 'logout'),
    path('lista/', views.lista_general, name = 'lista'),
    path('vehiculo/crear/', views.crear_vehiculo, name = 'crear_vehiculo'),
    path('conductor/eliminar/<int:pk>/', views.eliminar_conductor, name = 'eliminar_conductor'),
    path('conductor/actualizar/<int:pk>/', views.actualizar_conductor, name = 'update_conductor'),
    path('conductor/crear/', views.crear_conductor, name = 'crear_conductor'),
    path('despacho/', views.despacho, name = 'despacho'),
    path('despacho/crear/<int:pk>', views.procesar, name = 'procesar'),
    path('venta/', views.venta_lista, name = 'ventas'),
]