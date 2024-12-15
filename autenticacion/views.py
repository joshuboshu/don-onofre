from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError

class VRegistro(View):
    def get(self, request):
        return render(request, "registro/registro.html")

    def post(self, request):
        username = request.POST.get("username", '').strip()
        password = request.POST.get("password", '')
        confirm_password = request.POST.get("confirm_password", '')
        
        # Validación de campos vacíos
        if not username or not password or not confirm_password:
            messages.error(request, "Por favor, completa todos los campos.")
            return render(request, "registro/registro.html")

        # Validación de longitud de usuario
        if len(username) < 3:
            messages.error(request, "El nombre de usuario debe tener al menos 3 caracteres.")
            return render(request, "registro/registro.html")

        # Validación de longitud de contraseña
        if len(password) < 8:
            messages.error(request, "La contraseña debe tener al menos 8 caracteres.")
            return render(request, "registro/registro.html")

        # Validación de contraseñas coincidentes
        if password != confirm_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, "registro/registro.html")

        try:
            # Verificar si el usuario ya existe
            if User.objects.filter(username=username).exists():
                messages.error(request, "Este nombre de usuario ya está en uso. Por favor, elige otro.")
                return render(request, "registro/registro.html")

            # Crear el usuario
            user = User.objects.create_user(username=username, password=password)
            user.save()
            
            messages.success(request, "¡Cuenta creada exitosamente! Por favor, inicia sesión.")
            return redirect('logear')

        except IntegrityError:
            messages.error(request, "Hubo un problema al crear la cuenta. Por favor, intenta con un nombre de usuario diferente.")
        except Exception:
            messages.error(request, "Hubo un error inesperado. Por favor, intenta nuevamente más tarde.")
        
        return render(request, "registro/registro.html")
        
def cerrar_sesion(request):
    logout(request)
    return redirect('Home')

def logear(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("Home")
        else:
            messages.error(request, "Credenciales incorrectas")
    
    return render(request, "login/login.html")
