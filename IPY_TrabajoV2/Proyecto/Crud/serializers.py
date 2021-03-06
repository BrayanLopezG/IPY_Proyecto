from rest_framework import serializers
from .models import Conductor,Vehiculo,Venta,Postventa,Despacho

class ConductorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class VehiculoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'

class VentaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

class DespachoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Despacho
        fields = '__all__'
    
class PostventaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Postventa
        fields = '__all__'