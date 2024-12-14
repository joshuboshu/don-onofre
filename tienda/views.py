from django.shortcuts import render
from .models import Producto, CategoriaProd


def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()  # Obtener todas las categorías
    return render(request, "tienda/tienda.html", {"productos": productos, "categorias": categorias})
