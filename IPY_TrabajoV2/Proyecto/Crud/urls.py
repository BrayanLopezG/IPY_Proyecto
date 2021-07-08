from django.urls import path
from django.urls.conf import include
from .import views

urlpatterns = [
    #URL Conductor
    path('conductor/',views.ConductorLista,name="conductor_lista"),
    path('conductor/detalle/<int:pk>/',views.ConductorDetalle,name="conductor_detalle"),
    path('conductor/crear/',views.ConductorCrear,name="conductor_crear"),
    path('conductor/actualizar/<int:pk>/',views.ConductorActualizar,name="conductor_actualizar"),
    path('conductor/eliminar/<int:pk>/',views.ConductorEliminar,name="conductor_eliminar"),
    #URL Vehiculo
    path('vehiculo/',views.VehiculoLista,name="vehiculo_lista"),
    path('vehiculo/detalle/<int:pk>/',views.VehiculoDetalle, name="vehiculo_detalle"),
    path('vehiculo/crear/',views.VehiculoCrear,name="vehiculo_crear"),
    path('vehiculo/actualizar/<int:pk>/',views.VehiculoActualizar,name="vehiculo_actualizar"),
    path('vehiculo/eliminar/<int:pk>/',views.VehiculoEliminar,name="vehiculo_eliminar"),
    #URL Venta
    path('venta/',views.VentaLista,name="venta_lista"),
    path('venta/detalle/<int:pk>/',views.VentaDetalle, name="venta_detalle"),
    path('venta/crear/',views.VentaCrear,name="venta_crear"),
    path('venta/actualizar/<int:pk>/',views.VentaActualizar,name="venta_actualizar"),
    path('venta/eliminar/<int:pk>/',views.VentaEliminar,name="venta_eliminar"),
    #URL Despacho
    path('despacho/',views.DespachoLista,name="despacho_lista"),
    path('despacho/detalle/<int:pk>/',views.DespachoDetalle, name="despacho_detalle"),
    path('despacho/crear/',views.DespachoCrear,name="despacho_crear"),
    path('despacho/actualizar/<int:pk>/',views.DespachoActualizar,name="despacho_actualizar"),
    path('despacho/eliminar/<int:pk>/',views.DespachoEliminar,name="despacho_eliminar"),
    # URL Postventa
    path('postventa/',views.Postventa_lista, name = "postventa_lista"),
    path('postventa/crear/', views.Postventa_crear, name = "postventa_crear"),
    path('postventa/actualizar/<int:pk>/', views.Postventa_actualizar, name = "postventa_actualizar"),
    path('postventa/eliminar/<int:pk>/',views.Postventa_eliminar, name = "postventa_eliminar"),
]
