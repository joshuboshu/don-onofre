from django.shortcuts import render
from .models import Post, Categoria

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import CategoriaSerializer, PostSerializer

class CategoriaList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class PostsByCategoria(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, categoria_id):
        categoria = Categoria.objects.get(id=categoria_id)
        posts = Post.objects.filter(categorias=categoria)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


# Create your views here.
def blog(request):
    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {"categoria": categoria, "posts": posts})