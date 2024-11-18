from django.urls import path
from proyectoweb.consumers import LiveUpdateConsumer 

websocket_urlpatterns = [
    path('ws/live-update/', LiveUpdateConsumer.as_asgi()),
]
