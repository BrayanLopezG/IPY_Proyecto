from django.shortcuts import render
from rest_framework.response import Response
from .models import Conductor,Vehiculo
from .serializers import ConductorSerializers,VehiculoSerializers
from rest_framework.decorators import api_view

# Create your views here.

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