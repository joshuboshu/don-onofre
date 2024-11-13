from django.contrib.auth.models import User
from django.db import models

# No necesitamos un modelo personalizado a menos que quieras agregar campos adicionales.
# Si deseas un modelo extendido, puedes usar el siguiente ejemplo:

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Añade campos adicionales si lo deseas, por ejemplo:
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username
