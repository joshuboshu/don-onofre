from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Producto, CategoriaProd
from django.contrib.auth.decorators import login_required
from rules.contrib.views import permission_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductoSerializer, CategoriaProdSerializer
from rest_framework.permissions import IsAuthenticated



def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProd.objects.all()  # Obtener todas las categorías
    return render(request, "tienda/tienda.html", {"productos": productos, "categorias": categorias})


@login_required
@permission_required('tienda.add_categoriaprod', raise_exception=True)
def agregar_categoria(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        if nombre:
            CategoriaProd.objects.create(nombre=nombre)
            return JsonResponse({"success": True, "message": "Categoría agregada exitosamente."})
        return JsonResponse({"success": False, "message": "Nombre de categoría es obligatorio."})

    return render(request, "tienda/agregar_categoria_form.html")


@login_required
@permission_required('tienda.delete_producto', raise_exception=True)
def eliminar_producto(request, producto_id):
    if request.method == 'POST':
        try:
            producto = Producto.objects.get(id=producto_id)
            producto.delete()
            return JsonResponse({'success': True, 'message': 'Producto eliminado correctamente.'})
        except Producto.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Producto no encontrado.'})
    return JsonResponse({'success': False, 'message': 'Método no permitido.'})



@login_required
@permission_required('tienda.add_producto', raise_exception=True)
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


class CategoriaProdListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        categorias = CategoriaProd.objects.all()
        serializer = CategoriaProdSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaProdSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)