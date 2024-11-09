from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Producto, CategoriaProd


def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()  # Obtener todas las categorías
    return render(request, "tienda/tienda.html", {"productos": productos, "categorias": categorias})


def agregar_categoria(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        if nombre:
            CategoriaProd.objects.create(nombre=nombre)
            return JsonResponse({"success": True, "message": "Categoría agregada exitosamente."})
        return JsonResponse({"success": False, "message": "Nombre de categoría es obligatorio."})

    return render(request, "tienda/agregar_categoria_form.html")

def agregar_producto(request):
    categorias = CategoriaProd.objects.all()
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        categoria_id = request.POST.get("categorias")
        precio = request.POST.get("precio")
        disponibilidad = request.POST.get("disponibilidad") == 'on'
        imagen = request.FILES.get("imagen")

        if nombre and categoria_id and precio:
            categoria = get_object_or_404(CategoriaProd, id=categoria_id)
            Producto.objects.create(
                nombre=nombre,
                categorias=categoria,
                imagen=imagen,
                precio=precio,
                disponibilidad=disponibilidad,
            )
            return JsonResponse({"success": True, "message": "Producto agregado exitosamente."})
        return JsonResponse({"success": False, "message": "Todos los campos son obligatorios."})

    return render(request, "tienda/agregar_producto_form.html", {"categorias": categorias})