from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .carro import Carro
from tienda.models import Producto
from django.http import JsonResponse

# Create your views here.
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")

def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")

@require_POST
def update_cart(request):
    carro = Carro(request)
    product_id = request.POST.get('product_id')
    action = request.POST.get('action')
    
    try:
        producto = Producto.objects.get(id=product_id)
        
        if action == 'add':
            carro.agregar(producto)
        elif action == 'subtract':
            carro.restar_producto(producto)
        elif action == 'remove':
            carro.eliminar(producto)
        
        product_data = carro.carro.get(str(product_id), None)
        total = sum(float(item['precio']) for item in carro.carro.values())
        
        return JsonResponse({
            'success': True,
            'quantity': product_data['cantidad'] if product_data else 0,
            'price': product_data['precio'] if product_data else 0,
            'total': total,
            'cart_empty': len(carro.carro) == 0
        })
    except Producto.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Producto no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def cart_view(request):
    carro = Carro(request)
    return render(request, 'carro/carro.html', {'carro': carro})
