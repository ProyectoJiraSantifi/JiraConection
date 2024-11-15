"""
Clase Producto

Atributos:
    - idProducto (int): Identificador unico del producto.
    - nombre (str): Nombre del producto.
    - descripcion (str): Descripcion detallada del producto.
    - precio (float): Precio unitario del producto.
    - stock (int): Cantidad total de unidades disponibles en el inventario.
    - calificaciones (list<Calificacion>): Lista de calificaciones asignadas al producto.
    - cantidad (int): Cantidad seleccionada del producto en el carrito (inicialmente 0).

Metodos:
    - obtenerDetalles(): Devuelve la informacion detallada del producto, incluyendo el nombre, descripcion, precio y stock disponible.
    - actualizarStock(cantidad: int): Actualiza la cantidad de unidades disponibles en el stock del producto segun la cantidad agregada o eliminada 
    del carrito.

Relacion con otras clases:
    - Carrito:
        - Relacion de uno a muchos entre Producto y Carrito.
        - Cada carrito puede contener multiples productos, permitiendo al usuario seleccionar la cantidad deseada de cada uno.
        - La cantidad de cada producto en el carrito puede ser ajustada, incrementando o disminuyendo su valor según la acción del usuario.
        - El carrito accede a los atributos precio y cantidad de cada Producto para calcular el subtotal de cada producto y el total a pagar por 
        todos los productos.
        - Cuando un producto es agregado o eliminado del carrito se ajusta el inventario disponible utilizando el metodo actualizarStock() de Producto.

Clase Carrito

Atributos:
    - idCarrito (int): Identificador unico del carrito de compras.
    - usuario (Usuario): Referencia al usuario propietario del carrito.
    - listaProductos (list<Producto>): Lista de productos que el usuario ha agregado al carrito.
    - subtotal (float): Subtotal actual del carrito, calculado en funcion de los productos y sus cantidades.

Métodos:
    - agregarProducto(producto: Producto, cantidad: int): Agrega un producto al carrito con la cantidad especificada. Si el producto 
    ya está en el carrito, incrementa su cantidad.
    - eliminarProducto(producto: Producto): Elimina un producto específico del carrito, reduciendo el subtotal en consecuencia.
    - calcularSubtotal(): Calcula el subtotal del carrito sumando los precios multiplicados por la cantidad de cada producto en listaProductos.
    - vaciarCarrito(): Elimina todos los productos del carrito y restablece el subtotal a cero.
    - obtenerTotal(): Calcula y devuelve el total final del carrito, incluyendo el subtotal y cualquier otro cargo adicional que se defina en el futuro.

Relacion con otras clases:
    - Producto:
        - Relacion de uno a muchos entre Carrito y Producto.
        - Cada carrito puede contener multiples productos, y cada producto puede estar en varios carritos de diferentes usuarios.
        - La cantidad de cada producto en el carrito se administra en listaProductos, donde se puede incrementar o disminuir segun las interacciones del usuario.
        - Al agregar o eliminar productos, el carrito utiliza los atributos precio y cantidad de Producto para calcular el subtotal y el total.
        - El método agregarProducto() verifica el stock disponible del producto antes de añadirlo al carrito, utilizando actualizarStock() para reflejar 
        la cantidad disponible en el inventario.
   
"""