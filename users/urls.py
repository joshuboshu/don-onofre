from django.urls import path
from . import views

urlpatterns = [
    # Otras rutas
    path('profile/', views.profile, name='profile'),
]
