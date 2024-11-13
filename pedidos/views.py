from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Pedido, LineaPedido
from .serializers import PedidoSerializer
from carro.carro import Carro

from .adamspay_utils import create_debt, get_debt_status, is_debt_paid, get_payment_time


@login_required(login_url="/autenticacion/logear")
def checkout(request):
    carro = Carro(request)
    if not carro.carro:
        return redirect("Tienda")
    importe_total = carro.get_total_price()
    return render(request, 'pedidos/checkout.html', {'importe_total_carro': importe_total})

@login_required(login_url="/autenticacion/logear")
def procesar_pedido(request):
    if request.method == 'POST':
        carro = Carro(request)
        if not carro.carro:
            messages.error(request, "Tu carrito está vacío")
            return redirect("Tienda")

        pedido = Pedido.objects.create(user=request.user)
        lineas_pedido = []
        for key, value in carro.carro.items():
            lineas_pedido.append(LineaPedido(
                user=request.user,
                producto_id=key,
                pedido=pedido,
                cantidad=value["cantidad"],
            ))
        LineaPedido.objects.bulk_create(lineas_pedido)

        try:
            debt_response = create_debt(
                amount=int(carro.get_total_price()),
                label=f'Pedido {pedido.id}',
                doc_id=str(pedido.id)
            )
            if "debt" in debt_response and "payUrl" in debt_response["debt"]:
                pedido.adamspay_id = debt_response["debt"]["docId"]
                pedido.save()
                # Redirigir al usuario a la URL de pago de AdamsPay
                return redirect(debt_response["debt"]["payUrl"])
            else:
                raise Exception("No se pudo obtener la URL de pago de AdamsPay")
        except Exception as e:
            pedido.delete()
            messages.error(request, f"Error al procesar el pago: {str(e)}")
            return redirect("Tienda")

    return redirect("Tienda")

@login_required(login_url="/autenticacion/logear")
def confirmacion_pago(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id, user=request.user)
    debt_status = get_debt_status(pedido.adamspay_id)
    
    if is_debt_paid(debt_status):
        pedido.adamspay_status = "paid"
        payment_time = get_payment_time(debt_status)
        if payment_time:
            pedido.paid_at = payment_time
        pedido.save()

        carro = Carro(request)
        carro.limpiar_carro()

        messages.success(request, "El pago se ha completado con éxito.")
        return render(request, 'pedidos/confirmacion.html', {'pedido': pedido})
    else:
        messages.warning(request, "El pago aún no se ha completado.")
        return redirect('Tienda')

def enviar_mail(**kwargs):
    asunto = "Gracias por tu pedido"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario": kwargs.get("nombreusuario"),
    })

    mensaje_texto = strip_tags(mensaje)
    from_email = "usuario_tienda@gmail.com"
    to = kwargs.get("emailusuario")

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)

class PedidoListCreate(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pedidos = Pedido.objects.filter(user=request.user)
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)

    def post(self, request):
        carro = Carro(request)
        if not carro.carro:
            return Response({"error": "El carrito está vacío."}, status=status.HTTP_400_BAD_REQUEST)

        pedido = Pedido.objects.create(user=request.user)
        lineas_pedido = [
            LineaPedido(
                user=request.user,
                producto_id=key,
                pedido=pedido,
                cantidad=value["cantidad"]
            )
            for key, value in carro.carro.items()
        ]
        LineaPedido.objects.bulk_create(lineas_pedido)

        serializer = PedidoSerializer(pedido)
        carro.limpiar_carro()
        return Response(serializer.data, status=status.HTTP_201_CREATED)