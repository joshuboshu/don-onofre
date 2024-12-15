class Carro:
    """
    Clase que representa el carrito de compras del usuario.
    Permite agregar, eliminar, actualizar y limpiar productos en el carrito, 
    así como calcular el total de productos y el precio total del carrito.
    """

    def __init__(self, request):
        """
        Inicializa el carrito con la sesión del usuario.

        Args:
            request: Objeto HttpRequest que contiene la sesión del usuario.
        """
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def agregar(self, producto):
        """
        Agrega un producto al carrito. Si el producto ya está en el carrito, 
        incrementa su cantidad y actualiza el precio total.

        Args:
            producto: Objeto Producto que se va a agregar al carrito.
        """
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] += 1
                    value["precio"] = float(value["precio"]) + producto.precio
                    break
        self.guardar_carro()

    def guardar_carro(self):
        """
        Guarda los cambios del carrito en la sesión del usuario.
        """
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        """
        Elimina un producto del carrito.

        Args:
            producto: Objeto Producto que se va a eliminar del carrito.
        """
        producto.id = str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()

    def restar_producto(self, producto):
        """
        Resta la cantidad de un producto en el carrito. Si la cantidad llega a cero,
        el producto se elimina del carrito.

        Args:
            producto: Objeto Producto cuya cantidad se va a restar en el carrito.
        """
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] -= 1
                value["precio"] = float(value["precio"]) - producto.precio
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        """
        Limpia el carrito de compras, eliminando todos los productos.
        """
        self.session["carro"] = {}
        self.session.modified = True

    def get_total_price(self):
        """
        Calcula el precio total de todos los productos en el carrito.

        Returns:
            float: El precio total del carrito.
        """
        return sum(float(item['precio']) * item['cantidad'] for item in self.carro.values())

    def cantidad_total(self):
        """
        Devuelve la cantidad total de productos en el carrito.

        Returns:
            int: El total de productos en el carrito.
        """
        return sum(item['cantidad'] for item in self.carro.values())
