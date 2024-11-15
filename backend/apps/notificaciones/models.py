""" 
Modelo de Notificacion

Atributos
    - idNotificacion: Llave primaria, entero
    - mensaje: String
    - fechaEnvio: Date
    - usuario: Usuario
    
Metodos 
    + programarRecordatorio(): Metodo que programa un recordatorio para el administrador o para enviar
    mendajes a los usuarios al confirmar un pedido.
    
Conexiones
    Usuario:
        Conexion de 1 a muchos donde un usuario puede tener muchas notificaciones y una notificacion pertenece a un solo usuario

"""
