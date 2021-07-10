from django.db import models
from django.utils import timezone
from django.urls import reverse
import geocoder

token = 'pk.eyJ1IjoiYnJheWFubG1sIiwiYSI6ImNrcXNyOWl1YTA1YzQydXNiNXlwdWZsb2UifQ.pA4JkLi_o-OsuuG6ePvPdw'

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
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET_NULL,null=True)
    estado = models.ForeignKey(Estado, on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'Conductor'

    def __str__(self):
        return self.rut

class EstadoCompra(models.Model):
    descripcion = models.CharField(max_length=100, default='ESTADO')

    def __str__(self):
        return self.descripcion

class Venta(models.Model):
    nombre_cliente = models.CharField(max_length = 100,default = 'NOMBRE COMPLETO')
    rut_cliente = models.CharField(max_length = 11, default = 'RUT')
    direccion = models.CharField(max_length = 100, default = 'DIRECCION')
    nro_venta = models.CharField(max_length = 11, default = 'NUMERO VENTA')
    fecha_compra = models.DateField(auto_now=True)
    tipo_venta = models.CharField(max_length = 100, default = 'TIPO VENTA')
    estado_compra = models.ForeignKey(EstadoCompra,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.nro_venta
    
class Despacho(models.Model):
    nro_despacho = models.CharField(max_length = 5, default='NUMERO DESPACHO')
    venta = models.ForeignKey('Venta', on_delete=models.SET_NULL,null=True)
    conductor = models.ForeignKey('Conductor', on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.nro_despacho

class Postventa(models.Model):
    cliente = models.CharField(max_length = 100,default = 'NOMBRE COMPLETO')
    rut = models.CharField(max_length = 11, default = 'RUT')
    direccion = models.CharField(max_length = 100, default = 'DIRECCION')
    postventa = models.CharField(max_length = 11, default = 'NUMERO POSTVENTA')
    tipo_postventa = models.CharField(max_length = 100, default = 'TIPO POSTVENTA')
    estado_compra = models.ForeignKey(EstadoCompra,on_delete=models.SET_NULL,null=True)
    conductor = models.ForeignKey(Conductor,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.rut

class Direccion(models.Model):
    direccion = models.CharField(max_length=200)
    lat = models.CharField(max_length=100, blank=True, null=True)
    long = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *arg,**kwargs):
        g = geocoder.mapbox(self.direccion, key=token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Direccion,self).save(*arg,**kwargs)