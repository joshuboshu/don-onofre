from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Producto
from .forms import ProductoForm  

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos": productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            producto = form.save()
            return JsonResponse({
                'success': True,
                'producto': {
                    'id': producto.id,
                    'nombre': producto.nombre,
                    'precio': producto.precio,
                    'imagen_url': producto.imagen.url if producto.imagen else ''
                }
            })
        return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ProductoForm()
    return render(request, 'tienda/agregar_producto_form.html', {'form': form})
