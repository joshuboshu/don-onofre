import json
import http.client
from django.conf import settings
from datetime import datetime
from django.urls import reverse
from django.contrib.sites.models import Site

def create_debt(amount, label, doc_id):
    host = "staging.adamspay.com"
    path = "/api/v1/debts"
    headers = {
        "apikey": settings.ADAMSPAY_API_KEY,
        "Content-Type": "application/json"
    }

    base_url = settings.BASE_URL

    debt_data = {
        "amount": {
            "currency": "PYG",
            "value": str(amount)
        },
        "label": label,
        "docId": doc_id,
        "description": f"Pedido {doc_id}",
        "target": {
            "type": "web",
            "slug": settings.ADAMSPAY_WEBSITE_SLUG
        },
        "returnUrl": f"{base_url}{reverse('pedidos:confirmacion_pago', args=[doc_id])}",
        "cancelUrl": f"{base_url}{reverse('Tienda')}"
    }

    conn = http.client.HTTPSConnection(host)
    conn.request("POST", path, json.dumps(debt_data), headers)
    response = conn.getresponse()
    data = json.loads(response.read().decode("utf-8"))
    
    # Asegúrate de que la respuesta contiene la URL de pago
    if "debt" in data and "payUrl" in data["debt"]:
        return data
    else:
        raise Exception("No se pudo obtener la URL de pago de AdamsPay")

def get_debt_status(debt_id):
    host = "staging.adamspay.com" 
    path = f"/api/v1/debts/{debt_id}"
    headers = {"apikey": settings.ADAMSPAY_API_KEY}

    conn = http.client.HTTPSConnection(host)
    conn.request("GET", path, "", headers)
    response = conn.getresponse()
    data = response.read().decode("utf-8")
    return json.loads(data)

def is_debt_paid(debt_data):
    if "debt" in debt_data:
        debt = debt_data["debt"]
        pay_status = debt["payStatus"]["status"]
        return pay_status == "paid"
    return False

def get_payment_time(debt_data):
    if "debt" in debt_data and debt_data["debt"]["payStatus"]["status"] == "paid":
        return datetime.fromisoformat(debt_data["debt"]["payStatus"]["time"])
    return None