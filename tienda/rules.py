import rules

# Define reglas básicas
is_staff = rules.is_staff
is_authenticated = rules.is_authenticated

# Define permisos específicos para Producto
rules.add_perm('tienda.add_producto', is_staff)  # Solo staff puede agregar
rules.add_perm('tienda.view_producto', is_authenticated)  # Todos los autenticados pueden ver
rules.add_perm('tienda.delete_producto', is_staff)  # Solo staff puede eliminar

# Define permisos específicos para CategoriaProd (si lo necesitas)
rules.add_perm('tienda.add_categoriaprod', is_staff)
rules.add_perm('tienda.delete_categoriaprod', is_staff)