from rest_framework import serializers
from .models import CategoriaProd, Producto

class CategoriaProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProd
        fields = ['id', 'nombre', 'created', 'updated']

class ProductoSerializer(serializers.ModelSerializer):
    categorias = CategoriaProdSerializer()  # Si necesitas detalles completos de la categoría
    
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'categorias', 'imagen', 'precio', 'disponibilidad', 'created', 'updated']
