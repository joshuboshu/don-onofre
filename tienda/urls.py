from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name="Tienda"),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
]
