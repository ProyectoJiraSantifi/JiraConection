"""
Modelo de Producto

Atributos 
    - idPorudcto: Llave primaria, entero 
    - nombre: String 
    - descripcion: String
    - precio: Float
    - stock: Integer
    - calificaciones: lista de Calificacion
    - cantidad: Integer    

Metodos 
    + obtenerDetalles(): Metodo que despliega los detalles del producto
    + actualizarStock(cantidad: int): Metodo que actualiza el stock del producto

Conexiones
    Calificacion:
        Conexion de 1 a mucho donde un producto puede tener muchas calificaciones y una calificacion pertenece a un solo producto
    
    Carrito:
        Conexion de muchos a muchos donde muchos productos pueden estar en muchos carritos y muchos carritos pueden tener muchos productos
        
    Inventario:
        Conexion de 1 a muchos donde un producto puede estar en un solo inventario y un inventario puede tener muchos productos
        
    Pedido: 
        Conexion de 1 a muchos donde un producto puede estar en un solo pedido y un pedido puede tener muchos productos


Modelo de Carrito

Atributos
    - idCarrito: Llave primaria, entero
    - usuario: Usuario
    - listaProductos: lista de Producto
    - subtotal: Float
    
Metodos 
    + agregarProducto): Metodo que agrega un producto al carrito
    + eliminarProducto(): Metodo que elimina un producto del carrito
    + calcularSubtotal(): Metodo que calcula el subtotal del carrito
    + vaciarCarrito(): Metodo que permite eliminar por completo los productos del carrito
    + obtenerTotal(): Metodo que obtiene el total de la compra
    
Conexiones
    Usuario:
        Conexion de 1 a 1 donde un carrito pertenece a un solo usuario y un usuario tiene un solo carrito
    Producto:
        Conexion de muchos a muchos donde un carrito puede tener muchos productos y muchos productos pueden estar en muchos carritos
    Pedido: 
        Conexion de 1 a muchos donde un carrito puede tener muchos pedidos y un pedido pertenece a un solo carrito
        
"""
