from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect


@login_required
@csrf_protect
def password_change(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = request.user

        # Verificación de la contraseña actual
        if not user.check_password(old_password):
            return JsonResponse({'success': False, 'message': 'La contraseña actual es incorrecta.'})
        
        # Verificación de coincidencia de las nuevas contraseñas
        elif new_password != confirm_password:
            return JsonResponse({'success': False, 'message': 'Las nuevas contraseñas no coinciden.'})
        
        # Verificación de longitud mínima de la nueva contraseña
        elif len(new_password) < 8:
            return JsonResponse({'success': False, 'message': 'La nueva contraseña debe tener al menos 8 caracteres.'})
        
        # Cambiar la contraseña
        user.set_password(new_password)
        user.save()
        update_session_auth_hash(request, user)
        
        return JsonResponse({'success': True})
    
    return render(request, 'users/password_change.html')

@login_required
def profile(request):
    if request.method == 'POST':
        # Actualizar perfil
        username = request.POST.get('username')
        email = request.POST.get('email')

        user = request.user
        user.username = username
        user.email = email
        user.save()

        messages.success(request, 'Tu perfil ha sido actualizado con éxito')
        return redirect('profile')

    return render(request, 'users/profile.html', {'user': request.user})