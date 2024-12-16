from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .carro import Carro
from tienda.models import Producto
from django.template.loader import render_to_string

def agregar_producto(request, producto_id):
    """
    Agrega un producto al carrito de compras. Si el usuario no está autenticado, 
    devuelve un mensaje indicando que debe iniciar sesión.

    Args:
        request: Objeto HttpRequest que contiene los datos de la solicitud.
        producto_id: ID del producto que se va a agregar al carrito.

    Returns:
        JsonResponse: Respuesta JSON con el estado de la operación y el total de productos en el carrito.
    """
    if request.method == "POST":
        if not request.user.is_authenticated:
            return JsonResponse({
                "success": False,
                "message": "Debes iniciar sesión para agregar productos al carrito."
            })
        
        producto = get_object_or_404(Producto, id=producto_id)
        carro = Carro(request)
        carro.agregar(producto)
        
        # Obtener el número total de productos en el carrito
        total_productos = carro.cantidad_total()

        return JsonResponse({
            "success": True,
            "message": "Producto agregado al carrito.",
            "total_productos": total_productos  # Se incluye el total de productos en el carrito
        })
    
    return JsonResponse({"success": False, "message": "Método no permitido."})


def eliminar_producto(request, producto_id):
    """
    Elimina un producto del carrito de compras.

    Args:
        request: Objeto HttpRequest que contiene los datos de la solicitud.
        producto_id: ID del producto que se va a eliminar del carrito.

    Returns:
        redirect: Redirige al usuario a la vista de la tienda.
    """
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("Tienda")


def restar_producto(request, producto_id):
    """
    Resta la cantidad de un producto en el carrito. Si la cantidad es menor que 1, 
    el producto se elimina del carrito.

    Args:
        request: Objeto HttpRequest que contiene los datos de la solicitud.
        producto_id: ID del producto cuya cantidad se va a restar.

    Returns:
        redirect: Redirige al usuario a la vista de la tienda.
    """
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("Tienda")


def limpiar_carro(request):
    """
    Limpia todos los productos del carrito de compras.

    Args:
        request: Objeto HttpRequest que contiene los datos de la solicitud.

    Returns:
        redirect: Redirige al usuario a la vista de la tienda.
    """
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("Tienda")

@require_POST
def update_cart(request):
    """
    Actualiza el carrito de compras en función de la acción solicitada (agregar, restar, eliminar).
    Devuelve una respuesta JSON con la información actualizada del carrito.

    Args:
        request: Objeto HttpRequest que contiene los datos de la solicitud.

    Returns:
        JsonResponse: Respuesta JSON con los detalles del producto actualizado, el total y el HTML actualizado del carrito.
    """
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
        
        # Renderiza el HTML actualizado del carrito
        cart_html = render_to_string('carro/widget.html', {'carro': carro.carro}, request=request)
        
        return JsonResponse({
            'success': True,
            'quantity': product_data['cantidad'] if product_data else 0,
            'price': product_data['precio'] if product_data else 0,
            'name': producto.nombre,
            'total': total,
            'cart_empty': len(carro.carro) == 0,
            'cart_html': cart_html  # Incluye el HTML en la respuesta JSON
        })
    except Producto.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Producto no encontrado'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)


def cart_view(request):
    """
    Muestra la vista del carrito de compras con los productos añadidos.

    Args:
        request: Objeto HttpRequest que contiene los datos de la solicitud.

    Returns:
        render: Renderiza la plantilla del carrito con los productos actuales.
    """
    carro = Carro(request)
    return render(request, 'carro/carro.html', {'carro': carro})
