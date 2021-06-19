from django.contrib import admin
from .models import Vehiculo,Conductor,Estado,EstadoCompra,Venta,Despacho

# Register your models here.

admin.site.register(Vehiculo)
admin.site.register(Conductor)
admin.site.register(Estado)
admin.site.register(EstadoCompra)
admin.site.register(Venta)
admin.site.register(Despacho)
