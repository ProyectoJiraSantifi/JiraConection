"""
Modelo de Usuario

Atributos 
    - idUsuario: Llave primaria, entero 
    - nombre: String 
    - correo: String
    - contraseña: String
    - direccion: String
    - historialCompras: lista de Pedido
    
Metodos 
    + registrarse: Metodo que permite al usuario crear una nueva cuenta
    + iniciarSesion: Metodo que permite al usuario entrar a la plataforma
    + actualizarPerfil: Metodo que permite al usuario modificar detalles de su perfil

Conexiones
    Calificacion:
        Conexion de 1 a mucho donde un usuario puede poner muchas calificaciones y una o muchas calificaciones pertencen a un usuario.
    
    Carrito:
        Conexion de uno a uno donde un usuario tiene un carrito y un carrtio pertenece a un usuario.
        
    Notificacion:
        Conexion de 1 a muchos donde un usuario puede recibir una a muchas notificaciones y una o muchas notificaciones pueden enviarse a un usuario.
    Pedido: 
        Conexion de 1 a muchos donde un usuario puede tener uno a muchos pedidos y muchos o un pedido puede pertenecer a un usuario.

"""
