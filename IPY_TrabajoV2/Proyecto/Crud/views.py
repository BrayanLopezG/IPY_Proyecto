from ServicioWeb.views import despacho
from django.shortcuts import render
from rest_framework import serializers,viewsets
from rest_framework.response import Response
from .models import Conductor,Vehiculo,Venta,Despacho
from .serializers import ConductorSerializers,VehiculoSerializers,VentaSerializers,DespachoSerializers
from rest_framework.decorators import api_view

# Create your views here.

class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializers

class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializers

class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializers

class DespachoViewSet(viewsets.ModelViewSet):
    queryset = Despacho.objects.all()
    serializer_class = DespachoSerializers

#Conductor

@api_view(['GET'])

def ConductorLista(request):
    conductor = Conductor.objects.all()
    serializer = ConductorSerializers(conductor, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def ConductorDetalle(request,pk):
    conductor = Conductor.objects.get(id=pk)
    serializer = ConductorSerializers(conductor,many=False)
    return Response(serializer.data)

@api_view(['POST'])

def ConductorActualizar(request,pk):
    conductor = Conductor.objects.get(id=pk)
    serializer = ConductorSerializers(instance=conductor, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['POST'])

def ConductorCrear(request):
    serializer = ConductorSerializers(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])

def ConductorEliminar(request,pk):
    conductor = Conductor.objects.get(id=pk)
    conductor.delete()

    return Response('Eliminado')

#Vehiculo

@api_view(['GET'])

def VehiculoLista(request):
    vehiculo = Vehiculo.objects.all()
    serializer = VehiculoSerializers(vehiculo, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def VehiculoDetalle(request,pk):
    vehiculo = Vehiculo.objects.get(id=pk)
    serializer = VehiculoSerializers(vehiculo,many=False)
    return Response(serializer.data)

@api_view(['POST'])

def VehiculoActualizar(request,pk):
    vehiculo = Vehiculo.objects.get(id=pk)
    serializer = VehiculoSerializers(instance=vehiculo, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['POST'])

def VehiculoCrear(request):
    serializer = VehiculoSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])

def VehiculoEliminar(request,pk):
    vehiculo = Vehiculo.objects.get(id=pk)
    vehiculo.delete()

    return Response('Eliminado')

#Venta
@api_view(['GET'])

def VentaLista(request):
    venta = Venta.objects.all()
    serializer = VentaSerializers(venta, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def VentaDetalle(request,pk):
    venta = Venta.objects.get(id=pk)
    serializer = VentaSerializers(venta,many=False)
    return Response(serializer.data)

@api_view(['POST'])

def VentaActualizar(request,pk):
    venta = Venta.objects.get(id=pk)
    serializer = VentaSerializers(instance=venta, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['POST'])

def VentaCrear(request):
    serializer = VentaSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])

def VentaEliminar(request,pk):
    venta = Venta.objects.get(id=pk)
    venta.delete()

    return Response('Eliminado')

#Despacho
@api_view(['GET'])

def DespachoLista(request):
    despacho = Despacho.objects.all()
    serializer = DespachoSerializers(despacho, many=True)
    return Response(serializer.data)

@api_view(['GET'])

def DespachoDetalle(request,pk):
    despacho = Despacho.objects.get(id=pk)
    serializer = DespachoSerializers(despacho,many=False)
    return Response(serializer.data)

@api_view(['POST'])

def DespachoActualizar(request,pk):
    despacho = Despacho.objects.get(id=pk)
    serializer = DespachoSerializers(instance=despacho, data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['POST'])

def DespachoCrear(request):
    serializer = DespachoSerializers(data=request.data)

    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)

@api_view(['DELETE'])

def DespachoEliminar(request,pk):
    despacho = Despacho.objects.get(id=pk)
    despacho.delete()

    return Response('Eliminado')