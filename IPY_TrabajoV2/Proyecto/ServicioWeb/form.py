from django.forms import widgets
from django.forms.widgets import TextInput, Widget
from django import forms
from django.forms import ModelForm
from Crud.models import Conductor,Vehiculo,Estado

class ConductorForm(ModelForm):
    class Meta:
        model = Conductor 
        fields = ['rut','nombre','apellido','fono','vehiculo','estado']
    
class VehiculoForm(ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','color']