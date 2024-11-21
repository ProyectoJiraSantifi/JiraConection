""" 
Prueba de integracion de notificaciones: 

    funcion creacion:
        usuario = Nuevo usuario con nombre, correo, contraseña, direccion e historial de compras
        administrador = El administrador del sistema

    funcion probar notificacion:
        Se crea una nueva notificacion con el mensaje, la fecha de envio y el destinatario
        dependiendo de lo que se tenga que notificar. 
        
        se prueba que el usuario sea el mismo que el destinatario de la notificacion
        se prueba que el mensaje sea el mismo que el mensaje de la notificacion
        se prueba que la fecha de envio sea la misma que la fecha de envio de la notificacion
        
    probar programacion de notificaciones:
        Se crea una nueva notificaion con el mensaje, la fecha de envio y el destinatario
        dependiendo de lo que se tenga que notificar.
        
        se programa la notificacion para que se envie en una fecha especifica y se prueba que la fecha de envio sea la misma que la fecha programada
        se programa la notificacion para que se envie en una fecha especifica y se prueba que la fecha de envio sea menor a la fecha actual

Prueba de unidad: Módulo de Alertas de Inventario Bajo
1. Introducción

Propósito: Validar que el módulo de alertas funcione correctamente cuando el inventario de un producto esté por debajo del nivel mínimo establecido.
2. Alcance

Incluido: Generación de alertas para productos con inventario bajo.
3. Criterios de aceptación

    La alerta debe activarse cuando el inventario esté por debajo del umbral configurado.
    La alerta debe contener información del producto afectado.
    La alerta no debe activarse si el inventario está en el nivel mínimo o superior.

4. Casos de prueba
- ID de prueba: INV-001

    Descripción: Verificar que se genere una alerta cuando el inventario de un producto está por debajo del nivel mínimo.
    Precondiciones:
        El sistema tiene configurado un umbral de inventario mínimo (por ejemplo, 10 unidades).
        Existe un producto en el inventario con una cantidad inferior al umbral configurado.

Pasos a seguir:

    Configurar el umbral de inventario mínimo en 10 unidades.
    Registrar un producto con un inventario de 5 unidades.
    Ejecutar el sistema de monitoreo de alertas.

Resultado esperado:

    Se genera una alerta con el mensaje: "El inventario del producto [nombre del producto] está bajo el umbral mínimo."

Resultado real:
<Resultado de la operación>

Observaciones:
N/A

Aprobación:
Negada - Aprobada
- ID de prueba: INV-002

    Descripción: Verificar que no se genere una alerta cuando el inventario de un producto está en el nivel mínimo o superior.
    Precondiciones:
        El sistema tiene configurado un umbral de inventario mínimo (por ejemplo, 10 unidades).
        Existe un producto en el inventario con una cantidad igual o superior al umbral configurado.

Pasos a seguir:

    Configurar el umbral de inventario mínimo en 10 unidades.
    Registrar un producto con un inventario de 10 unidades.
    Ejecutar el sistema de monitoreo de alertas.

Resultado esperado:

    No se genera ninguna alerta.

Resultado real:
<Resultado de la operación>

Observaciones:
N/A

Aprobación:
Negada - Aprobada

"""
