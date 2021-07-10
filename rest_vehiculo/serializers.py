from rest_framework import serializers, fields
from app.models import Vehiculo

class VehiculoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['patente','marca','modelo','categoria']
        