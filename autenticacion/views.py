from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

class VRegistro(View):
    def get(self, request):
        return render(request, "registro/registro.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        if password == confirm_password:
            try:
                # Crear el usuario sin intentar autenticarlo inmediatamente
                user = User.objects.create_user(username=username, password=password)
                user.save()
                
                # Mensaje de éxito y redirección a la página de login
                messages.success(request, "Cuenta creada exitosamente. Por favor, inicia sesión.")
                return redirect('logear')  # Redirige a la vista de login
            except Exception as e:
                messages.error(request, f"Error al crear la cuenta: {str(e)}")
        else:
            messages.error(request, "Las contraseñas no coinciden")
        
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
