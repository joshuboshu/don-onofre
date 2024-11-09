from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto, CategoriaProd
from .forms import ProductoForm, CategoriaForm


def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()  # Obtener todas las categorías
    return render(request, "tienda/tienda.html", {"productos": productos, "categorias": categorias})


def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            categorias = CategoriaProd.objects.all()  # Obtener todas las categorías actualizadas
            # Crear una lista con los datos de las categorías
            categorias_data = [{'id': cat.id, 'nombre': cat.nombre} for cat in categorias]
            return JsonResponse({
                'success': True,
                'producto': {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio': producto.precio,
                    'imagen_url': producto.imagen.url if producto.imagen else ''
                },
                'categorias': categorias_data  # Enviar la lista de categorías actualizada
            })
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductoForm()
    return render(request, 'tienda/agregar_producto_form.html', {'form': form})


def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            categoria = form.save()
            categorias = CategoriaProd.objects.all()  # Obtener todas las categorías actualizadas
            # Crear una lista con los datos de las categorías
            categorias_data = [{'id': cat.id, 'nombre': cat.nombre} for cat in categorias]
            return JsonResponse({
                'success': True,
                'categoria': {
                    'id': categoria.id,
                    'nombre': categoria.nombre,
                },
                'categorias': categorias_data  # Enviar la lista de categorías actualizada
            })
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = CategoriaForm()
    return render(request, 'tienda/agregar_categoria_form.html', {'form': form})

