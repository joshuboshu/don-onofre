from rest_framework import serializers
from .models import Categoria, Post
from django.contrib.auth.models import User

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'created', 'updated']

class PostSerializer(serializers.ModelSerializer):
    categorias = CategoriaSerializer(many=True)  # Incluye detalles de categorías
    autor = serializers.StringRelatedField()  # Muestra el nombre del autor

    class Meta:
        model = Post
        fields = ['id', 'titulo', 'contenido', 'imagen', 'autor', 'categorias', 'created', 'updated']
