"""
Prueba funcional:  Clases de Pago
1 Introducción

Propósito: Validar que el sistema de procesamiento de pagos funcione correctamente, asegurando que los pagos se realicen y registren de manera adecuada.

2 Alcance

Incluido: Procesamiento de pagos utilizando métodos de pago válidos, actualización del estado de los pagos y validación del monto.
Excluido: Conexión a pasarelas de pago externas.


3 Criterios de aceptación:

El sistema debe procesar pagos solo si todos los datos requeridos son válidos.
El estado del pago debe actualizarse correctamente después de procesarlo.
En caso de error, se debe mostrar un mensaje claro al usuario.
Los pagos no válidos no deben ser procesados ni registrados.
--------------------------------------------------------------------------

Prueba 1: Validación de entrada en ProcesarPago()
Introducción
Propósito: Verificar que el método ProcesarPago() maneje correctamente entradas inválidas o datos faltantes.

Alcance
Incluido: Validación de parámetros como metododePago, monto y estado.
Excluido: Conexión a sistemas externos para procesar pagos reales.

Criterios de aceptación:

Se debe generar un error si los valores requeridos están ausentes o son inválidos.
El sistema no debe procesar pagos si hay parámetros incorrectos.
El mensaje de error debe ser claro y específico.
Casos de prueba

ID de prueba: SEG-001
Descripción: Enviar datos incompletos a ProcesarPago().
Precondiciones: El sistema debe estar configurado para aceptar valores válidos en metododePago y monto.
Pasos a seguir:
Llamar al método ProcesarPago() sin especificar el metododePago.
Llamar al método con monto como un valor negativo.
Llamar al método con un estado no permitido.
Resultado esperado:
Error específico indicando el parámetro faltante o inválido.
Resultado real:
Observaciones: N/A
Aprobación: Aprobada/Negada

-----------------------------------------------------------------------


Prueba 2 Autenticación en relación con IDUSUARIO
Introducción
Propósito: Garantizar que el atributo IDUSUARIO esté autenticado y asociado correctamente al usuario.

Alcance
Incluido: Validación de la relación de IDUSUARIO con un usuario activo en el sistema.
Excluido: Escenarios en los que el usuario esté eliminado.

Criterios de aceptación:

El método debe verificar que IDUSUARIO esté autenticado.
Los pagos asociados a usuarios no autenticados deben ser rechazados.
Casos de prueba

ID de prueba: SEG-002
Descripción: Intentar procesar un pago con un IDUSUARIO no válido o no autenticado.
Precondiciones: Base de datos configurada con usuarios válidos.
Pasos a seguir:
Crear un pago con un IDUSUARIO inexistente.
Intentar procesar el pago.
Resultado esperado:
Mensaje de error indicando la falta de autenticación del usuario.
Resultado real:
Observaciones: N/A
Aprobación: Aprobada/Negada

-------------------------------------------

Prueba 3 Seguridad de actualizaciones en el estado del pago
Introducción
Propósito: Validar que solo usuarios autorizados puedan cambiar el estado de un pago.

Alcance
Incluido: Actualización del atributo estado del pago.
Excluido: Funciones externas relacionadas con reportes.

Criterios de aceptación:

Cambios en el estado solo permitidos para usuarios con roles específicos.
Los intentos de cambio de estado no autorizados deben ser rechazados.
Casos de prueba

ID de prueba: SEG-003
Descripción: Intentar cambiar el estado de un pago sin los permisos adecuados.
Precondiciones: Sistema con roles y permisos configurados.
Pasos a seguir:
Iniciar sesión como usuario sin privilegios administrativos.
Intentar modificar el atributo estado de un pago.
Resultado esperado:
Error indicando falta de permisos.
Resultado real:
Observaciones: N/A
Aprobación: Aprobada/Negada

----------------------------------------------------------

Prueba 4 Integridad en la relación Pedido-Pago
Introducción
Propósito: Asegurar que un pago no pueda ser asociado a múltiples pedidos.

Alcance
Incluido: Validación de la relación uno a uno entre Pedido y Pago.
Excluido: Escenarios donde no existan pedidos asociados.

Criterios de aceptación:

Un pago debe estar asociado únicamente a un pedido.
Intentar asignar el mismo pago a múltiples pedidos debe generar un error.
Casos de prueba

ID de prueba: SEG-004
Descripción: Intentar asociar un pago existente a un nuevo pedido.
Precondiciones: Base de datos con pagos ya vinculados a pedidos.
Pasos a seguir:
Seleccionar un pago ya vinculado a un pedido.
Intentar asociarlo a otro pedido.
Resultado esperado:
Mensaje de error indicando la relación violada.
Resultado real:
Observaciones: N/A
Aprobación: Aprobada/Negada

"""

