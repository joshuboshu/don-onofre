from django.shortcuts import render
from .models import Producto, CategoriaProd
from carro.carro import Carro


def tienda(request):
    """
    Vista que renderiza la tienda con todos los productos y categorías.

    Obtiene todos los productos y categorías de la base de datos, además
    del estado actual del carrito, y los pasa al template correspondiente.

    Args:
        request: Objeto de solicitud HTTP.

    Returns:
        Renderiza el template 'tienda/tienda.html' con los productos,
        categorías y el estado actual del carrito.
    """
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()  # Obtener todas las categorías
    carro = Carro(request)  # Estado actual del carrito
    
    return render(request, "tienda/tienda.html", {
        "productos": productos,
        "categorias": categorias,
        "carro": carro
    })


def productos_por_categoria(request, categoria_id):
    """
    Vista que renderiza los productos de una categoría específica.

    Obtiene los productos que pertenecen a la categoría seleccionada por
    el usuario, así como todas las categorías y el estado actual del carrito.
    Luego, pasa esta información al template correspondiente.

    Args:
        request: Objeto de solicitud HTTP.
        categoria_id: ID de la categoría seleccionada.

    Returns:
        Renderiza el template 'tienda/tienda.html' con los productos filtrados
        por la categoría seleccionada, todas las categorías, la categoría actual
        y el estado actual del carrito.
    """
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
