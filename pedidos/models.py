from django.contrib.auth import get_user_model
from django.db import models
from tienda.models import Producto
from django.db.models import F, Sum, FloatField
# Create your models here.

User = get_user_model()

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    adamspay_id = models.CharField(max_length=255, blank=True, null=True)
    adamspay_status = models.CharField(max_length=50, blank=True, null=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Pedido {self.id}"
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F('precio')*F('cantidad'), output_field=FloatField())
        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']

class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, default=None)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        db_table = 'lineapedidos'
        verbose_name = 'linea pedido'
        verbose_name_plural = 'lineas pedidos'
        ordering = ['id']