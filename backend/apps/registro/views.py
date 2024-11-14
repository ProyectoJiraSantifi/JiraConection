"""
Edición de cuenta: Se va a poder añadir información adicional a la cuenta, como dirección de entrega, tarjeta
    que se usará para efectuar los pagos, teléfono de contacto, o bien poder visualizar elementos como la lista 
    de los pedidos realizados y su estado, carrito de compras y las calificaciones efectuadas. Así como la
    posibilidad de editar dicha información.

Formulario de registro: El usuario podrá registrar una cuenta que contenga un nombre de usuario,
    un correo existente que el cliente tenga, una contraseña, y el aceptar los términos y condiciones
    que vienen con crear dicha cuenta.
    
Inicio de sesión: Si el usuario ya está registrado, puede iniciar sesión usando su nombre de usuario 
    o correo y su contraseña. Si las credenciales existen, el sistema le permitirá entrar a la tienda sin
    problemas. Si la cuenta del usuario tiene activada la seguridad de 2-pasos, se le va a pedir el código 
    que este método otorga para una capa de seguridad extra.
    
En esta sección se van a presentar dos formularios para cada caso (Registro e inicio de sesión):
    Registro: Un formulario el cual solicita que se ingresen los siguientes datos para guardar en el sistema
        -Nombre de usuario
        -Correo anexo a la cuenta
        -Contraseña
        -Repetir contraseña
        -Botón para verificar el registro
        -Botón para regresar a la pantalla de inicio de sesión/Cancelar el registro
    
    Inicio de sesión: Formulario que solicita ingresar los siguientes datos para verificar si existe la cuenta
        -Nombre de usuario o correo
        -Contraseña
        -Botón para entrar
        -Botón para navegar al formulario de registro
        
    Visualización de cuenta: El usuario puede observar y modificar la información referente a su cuenta
        -Nombre de usuario
        -Correo
        -Contraseña
        -Teléfono
        -Método de pago
        -Dirección de entrega
        -Imágen de perfil
        -Activar la verificación de 2-pasos
        -Establecer un correo alterno de recuperación en caso de robo de la cuenta
"""