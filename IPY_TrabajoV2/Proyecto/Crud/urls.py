from django.urls import path
from .import views

urlpatterns = [
    path('conductor/',views.ConductorLista,name="Con_lista"),
    path('condetalle/<int:pk>/',views.ConductorDetalle,name="Con_detalle"),
    path('concrear',views.ConductorCrear,name="Con_crear"),
    path('conactualizar/<int:pk>/',views.ConductorActualizar,name="Con_actualizar"),
    path('coneliminar/<int:pk>/',views.ConductorEliminar,name="Con_eliminar"),
    path('vehiculo/',views.VehiculoLista,name="Veh_lista"),
    path('vehdetalle/<int:pk>/',views.VehiculoDetalle, name="Veh_detalle"),
    path('vehcrear',views.VehiculoCrear,name="Veh_crear"),
    path('vehactualizar/<int:pk>/',views.VehiculoActualizar,name="Veh_actualizar"),
    path('veheliminar/<int:pk>/',views.VehiculoEliminar,name="Veh_eliminar"),
]