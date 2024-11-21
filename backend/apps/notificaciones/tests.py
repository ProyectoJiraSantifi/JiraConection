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
"""

"""
Prueba de integración: Confirmación de pedidos.

1. Introducción.
    Propósito: Validar la correcta integración entre el módulo de confirmación de pedidos y el módulo de notificaciones para 
    garantizar que los usuarios reciban las notificaciones correspondientes cuando se confirma un pedido.

2. Alcance.
    Incluido: Confirmación de pedidos, generación y envío de notificaciones a los usuarios.

3. Criterios de aceptación:
    - Los usuarios deben recibir una notificación al confirmar su pedido.
    - Las notificaciones deben contener el mensaje correcto y enviarse en la fecha y hora programadas.
    - La notificación debe estar asociada al usuario correcto.
    - El sistema debe registrar correctamente las notificaciones generadas.

4. Casos de prueba.

    - ID de prueba: PI-001

    - Descripción: Verificar que al confirmar un pedido, se genere y envíe una notificación al usuario.

    - Precondiciones: 
        1. Existe un pedido en el sistema que se puede confirmar.
        2. El usuario está registrado y vinculado al pedido.

    Pasos a seguir:
    1. Confirmar un pedido en el sistema.
    2. Verificar que se genere una notificación para el usuario correspondiente.
    3. Revisar el contenido de la notificación para validar que sea correcto.
    4. Verificar que la notificación se haya enviado correctamente al usuario.

    Resultado esperado: 
        - Notificación generada con mensaje de confirmación correcto.
        - Notificación asociada al usuario correcto.
        - Notificación enviada exitosamente.

    Resultado real: Todas las operaciones se realizaron correctamente.

    Observaciones: N/A

    Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: PI-002

    - Descripción: Verificar que se registre correctamente la fecha y hora de envío de la notificación.

    - Precondiciones:
        1. Existe un pedido confirmado en el sistema.
        2. El módulo de notificaciones está activo.

    Pasos a seguir:
    1. Confirmar un pedido.
    2. Generar la notificación correspondiente.
    3. Verificar que la notificación registre la fecha y hora de envío correctamente.

    Resultado esperado: 
        - Fecha y hora de envío correctamente registradas en el sistema.

    Resultado real: Fecha y hora registradas correctamente.

    Observaciones: N/A

    Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: PI-003

    - Descripción: Verificar que se asocie correctamente la notificación al usuario correspondiente.

    - Precondiciones:
        1. Existe un usuario registrado y un pedido asociado a ese usuario.

    Pasos a seguir:
    1. Confirmar el pedido del usuario.
    2. Generar la notificación correspondiente.
    3. Verificar que la notificación esté asociada al usuario correcto en el sistema.

    Resultado esperado:
        - Notificación asociada correctamente al usuario correspondiente.

    Resultado real: Asociación realizada correctamente.

    Observaciones: N/A

    Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: PI-004

    - Descripción: Verificar que las notificaciones programadas para confirmar pedidos se envíen en el momento correcto.

    - Precondiciones:
        1. Existe una notificación programada para un pedido confirmado.

    Pasos a seguir:
    1. Confirmar un pedido y programar la notificación.
    2. Esperar hasta el momento programado para el envío.
    3. Verificar que la notificación se envíe correctamente.

    Resultado esperado:
        - Notificación enviada en el momento correcto según lo programado.

    Resultado real: Notificación enviada correctamente según lo programado.

    Observaciones: N/A

    Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: PI-005

    - Descripción: Verificar que el mensaje de la notificación sea adecuado y contenga la información necesaria.

    - Precondiciones:
        1. Existe un pedido confirmado.
        2. El sistema genera la notificación correspondiente.

    Pasos a seguir:
    1. Confirmar un pedido.
    2. Generar la notificación correspondiente.
    3. Verificar el contenido del mensaje para asegurarse de que sea adecuado y contenga la información necesaria (Ejemplo: número de pedido, estado del pedido, fecha).

    Resultado esperado:
        - El mensaje de la notificación contiene toda la información necesaria y está correctamente redactado.

    Resultado real: El mensaje de la notificación es adecuado y contiene toda la información necesaria.

    Observaciones: N/A

    Aprobación: Aprobada
"""
