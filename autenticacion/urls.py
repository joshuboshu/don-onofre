from django.urls import path
from .views import VRegistro, cerrar_sesion, logear
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('registro/', RegisterView.as_view(), name="registro"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    
    path('', VRegistro.as_view(), name="Autenticacion"),
    path('cerrar_sesion', cerrar_sesion, name="cerrar_sesion"),
    path('logear', logear, name="logear"),
]


