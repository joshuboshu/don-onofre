from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('procesar/', views.procesar_pedido, name="procesar_pedido"),
    path('confirmacion/<int:pedido_id>/', views.confirmacion_pago, name='confirmacion_pago'),
]
