from django.db import models
from django.utils import timezone

# Create your models here.
class Vehiculo(models.Model):
    patente = models.CharField(max_length=9,default='PATENTE')
    marca = models.CharField(max_length=100,default='MARCA')
    modelo = models.CharField(max_length=100,default='MODELO')
    color = models.CharField(max_length=100,default='COLOR')
    crearted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Vehiculo'

    def __str__(self):
        return self.patente

class Estado(models.Model):
    descripcion = models.CharField(max_length=100, default='ESTADO')

    class Meta:
        db_table = 'Estado'
    
    def __str__(self):
        return self.descripcion

class Conductor(models.Model):
    rut = models.CharField(max_length=11,default='RUT')
    nombre = models.CharField(max_length=100, default='NOMBRE')
    apellido = models.CharField(max_length=100, default='APELLIDO')
    fono = models.CharField(max_length=100, default='FONO')
    crearted_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    vehiculo = models.ForeignKey('Vehiculo', on_delete=models.SET_NULL,null=True)
    estado = models.ForeignKey('Estado', on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'Conductor'

    def __str__(self):
        return self.nombre
