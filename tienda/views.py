from django.shortcuts import render
from .models import Producto, CategoriaProd


def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()  # Obtener todas las categorías
    return render(request, "tienda/tienda.html", {"productos": productos, "categorias": categorias})


def productos_por_categoria(request, categoria_id):
    categoria = CategoriaProd.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria)
    return render(request, "carro/widget.html", {"categoria": categoria, "productos": productos})