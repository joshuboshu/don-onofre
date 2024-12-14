from django.urls import path
from . import views
from carro.views import agregar_producto, restar_producto, eliminar_producto

urlpatterns = [
    path('', views.tienda, name="Tienda"),
    path('categoria/<int:categoria_id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('agregar/<int:producto_id>/', agregar_producto, name="agregar_producto"),
    path('restar/<int:producto_id>/', restar_producto, name="restar_producto"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="eliminar_producto"),
]
