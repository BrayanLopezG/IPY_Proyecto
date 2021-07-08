from django.contrib import admin
from .models import Direccion, Postventa, Vehiculo,Conductor,Estado,EstadoCompra,Venta,Despacho

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Conductor)
admin.site.register(Estado)
admin.site.register(EstadoCompra)
admin.site.register(Venta)
admin.site.register(Postventa)
admin.site.register(Despacho)
admin.site.register(Direccion)