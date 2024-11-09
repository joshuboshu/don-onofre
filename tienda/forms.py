from django import forms
from .models import Producto, CategoriaProd

# Formulario para agregar productos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categorias', 'imagen', 'precio', 'disponibilidad']  # Cambié 'categoria' por 'categorias'
        widgets = {
            'disponibilidad': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# Formulario para agregar categorías
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = CategoriaProd
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
        }
