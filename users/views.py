from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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