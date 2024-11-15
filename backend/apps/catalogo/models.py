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

"""
