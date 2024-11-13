from rest_framework import serializers
from .models import Servicio

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['id', 'titulo', 'contenido', 'imagen', 'created', 'updated']
