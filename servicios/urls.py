from django.urls import path
from . import views
from .views import ServicioList

urlpatterns = [
    path('', views.servicios, name="Servicios"),
    path('api/servicios/', ServicioList.as_view(), name='servicio-list'),
]