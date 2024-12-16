from django.db import models

class CategoriaProd(models.Model):
    """
    Modelo que representa una categoría de productos en la tienda.
    """
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'categoriaProd'
        verbose_name_plural = 'categoriasProd'

    def __str__(self):
        """
        Retorna el nombre de la categoría como representación de texto.
        """
        return self.nombre


class Producto(models.Model):
    """
    Modelo que representa un producto en la tienda.
    Cada producto puede pertenecer a una categoría y tener características.
    """
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda/", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """
        Retorna el nombre del producto como representación de texto.
        """
        return self.nombre


class Caracteristica(models.Model):
    """
    Modelo que representa las características de un producto.
    Un producto puede tener muchas características.
    """
    producto = models.ForeignKey(Producto, related_name='caracteristicas', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    valor = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Caracteristica'
        verbose_name_plural = 'Características'

    def __str__(self):
        """
        Retorna el nombre y el valor de la característica como representación de texto.
        """
        return f"{self.nombre}: {self.valor}"
