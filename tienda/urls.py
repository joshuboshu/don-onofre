from django.urls import path
from . import views

urlpatterns = [
    path('', views.tienda, name="Tienda"),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
]
