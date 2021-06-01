from rest_framework import serializers
from .models import Conductor,Vehiculo

class ConductorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = '__all__'

class VehiculoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'
