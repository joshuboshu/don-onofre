from django.shortcuts import render
from .models import Producto, CategoriaProd
from carro.carro import Carro
from django.http import JsonResponse

def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()  # Obtener todas las categorías
    carro = Carro(request)  # Estado actual del carrito
    return render(request, "tienda/tienda.html", {"productos": productos, "categorias": categorias, "carro": carro})


def productos_por_categoria(request, categoria_id):
    categoria = CategoriaProd.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria)
    carro = Carro(request)  # Estado actual del carrito
    return render(request, "tienda/tienda.html", {"productos": productos, "categoria": categoria, "carro": carro})
