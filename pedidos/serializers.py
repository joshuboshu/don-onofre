from rest_framework import serializers
from .models import Pedido, LineaPedido

class LineaPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaPedido
        fields = ['id', 'user', 'producto', 'pedido', 'cantidad', 'created_at']

class PedidoSerializer(serializers.ModelSerializer):
    lineas = LineaPedidoSerializer(many=True, read_only=True, source='lineapedido_set')
    total = serializers.FloatField()

    class Meta:
        model = Pedido
        fields = ['id', 'user', 'created_at', 'adamspay_id', 'adamspay_status', 'paid_at', 'total', 'lineas']
