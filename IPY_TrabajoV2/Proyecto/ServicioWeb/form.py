from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from Crud.models import Conductor,Vehiculo,Despacho,Venta,Direccion

class ConductorForm(ModelForm):
    class Meta:
        model = Conductor 
        fields = ['rut','nombre','apellido','fono','vehiculo','estado']
    
class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','color']
    
class DespachoForm(ModelForm):
    class Meta:
        model = Despacho
        fields = ['nro_despacho','venta','conductor']

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        fields = ['estado_compra']

class AsignarConductorForm(ModelForm):
    class Meta:
        model = Conductor
        fields = ['estado']
    
class DireccionForm(ModelForm):
    class Meta:
        model = Direccion
        fields = ['direccion']