from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categorias', 'imagen', 'precio', 'disponibilidad']  # Cambié 'categoria' por 'categorias'
        widgets = {
            'disponibilidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
