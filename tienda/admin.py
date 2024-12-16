from django.contrib import admin
from .models import CategoriaProd, Producto, Caracteristica


class CaracteristicaInline(admin.TabularInline):
    """
    Modelo Inline para administrar características de un producto desde su panel de edición.
    """
    model = Caracteristica
    extra = 1  # Número de formularios vacíos que se muestran por defecto


class CategoriaProdAdmin(admin.ModelAdmin):
    """
    Configuración para la administración de las categorías de productos.
    """
    readonly_fields = ("created", "updated")


class ProductoAdmin(admin.ModelAdmin):
    """
    Configuración para la administración de productos.
    """
    readonly_fields = ("created", "updated")
    list_display = ('nombre', 'precio', 'disponibilidad', 'categorias')  # Mostrar campos clave en la lista
    search_fields = ('nombre',)  # Habilitar búsqueda por nombre del producto
    inlines = [CaracteristicaInline]  # Incluir Inline para características


class CaracteristicaAdmin(admin.ModelAdmin):
    """
    Configuración para la administración de características de los productos.
    """
    list_display = ('producto', 'nombre', 'valor')  # Mostrar producto, nombre y valor de la característica
    search_fields = ('producto__nombre', 'nombre')  # Buscar por nombre del producto y nombre de la característica


# Registrar los modelos con sus configuraciones en el admin
admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Caracteristica, CaracteristicaAdmin)
