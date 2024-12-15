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
    categorias = CategoriaProd.objects.all()  # Obtener todas las categorías
    categoria_actual = CategoriaProd.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria_actual)
    carro = Carro(request)
    
    return render(request, "tienda/tienda.html", {
        "productos": productos,
        "categorias": categorias,  # Pasamos todas las categorías
        "categoria_actual": categoria_actual,  # Categoría seleccionada actualmente
        "carro": carro
    })
