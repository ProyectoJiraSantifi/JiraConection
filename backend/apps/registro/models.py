"""
Modelo de Usuario

Atributos
    - idUsuario: Llave primaria, entero
    - nombreUsuario: String
    - correoElectronico: String, único
    - contrasena: String
    - direccionEnvio: String
    - telefono: String
    - pedidos: lista de Pedido
    - carritos: lista de Carrito
    - calificaciones: lista de Calificacion

Métodos
    + registrarUsuario(): Método que registra al usuario en el sistema
    + iniciarSesion(correo: String, contrasena: String): Método que valida y permite el acceso al sistema
    + actualizarDatos(nombre: String, correo: String, direccion: String, telefono: String): Método para actualizar datos personales del usuario
    + agregarDireccionEnvio(direccion: String): Método para añadir o modificar la dirección de envío del usuario
    + obtenerHistorialPedidos(): Método que devuelve una lista de todos los pedidos del usuario
    + obtenerDetallesUsuario(): Método que despliega los detalles del usuario, incluyendo nombre, dirección y teléfono

Conexiones
    Pedido:
        Relación de 1 a muchos. Un usuario puede tener muchos pedidos, pero cada pedido pertenece a un solo usuario.

    Carrito:
        Relación de 1 a muchos. Un usuario puede tener múltiples carritos activos o inactivos, pero cada carrito pertenece a un solo usuario.

    Calificacion:
        Relación de 1 a muchos. Un usuario puede realizar varias calificaciones a productos diferentes, y cada calificación pertenece a un solo usuario.
"""