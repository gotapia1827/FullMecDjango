from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import Vehiculo
from .serializers import VehiculoSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_vehiculos(request):
    """
    lista  todos los vehiculos
    """
    if request.method == 'GET':
        vehiculo = Vehiculo.objects.all()
        serializers = VehiculoSerializers(vehiculo, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializers = VehiculoSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def detalle_vehiculo(request, id):
    """
    Get,Update o delete vehiculo
    """
    try:
        vehiculo = Vehiculo.objects.get(patente=id)
    except Vehiculo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = VehiculoSerializers(vehiculo)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehiculoSerializers(vehiculo,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vehiculo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

