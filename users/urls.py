from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas
    path('profile/', views.profile, name='profile'),
    path('cambiar-contrasena/', views.password_change, name='password_change'),

]
