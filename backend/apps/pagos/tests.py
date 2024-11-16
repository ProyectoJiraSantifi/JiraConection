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

"""

Generalización para pruebas funcionales y de seguridad del modelo de pago

1 Introducción

Propósito: Validar que el modelo de pago funcione correctamente y cumpla con los estándares funcionales y de seguridad al procesar pagos, verificarlos y gestionar su relación con los pedidos, considerando la integración con plataformas como PayPal y Mercado Libre.

2 Alcance

Incluido:
Procesamiento de pagos mediante procesarPagoConPayPal() y procesarPagoConMercadoLibre().
Validación del estado de los pagos mediante verificarPago().
Relación uno a uno entre Pedido y Pago.
Manejo seguro de datos sensibles (tokens, credenciales).
Excluido: Validaciones internas de las plataformas externas (PayPal y Mercado Libre).

3 Criterios de aceptación:

Los pagos deben procesarse solo con datos válidos.
El sistema debe manejar correctamente la comunicación con las plataformas externas.
Los estados de los pagos deben actualizarse correctamente tras la verificación.
Los datos sensibles deben estar cifrados y protegidos contra accesos no autorizados.
Cada pago debe estar vinculado exclusivamente a un único pedido.
En caso de error, el sistema debe mostrar mensajes claros sin exponer información técnica.


-------------------------------------------------------------------------

Prueba de interfaz de usuario: Redirección a PayPal

1 Introducción

* Propósito: Validar que la redirección al formulario de pago de PayPal se realice correctamente desde la interfaz del sistema.

2 Alcance

* Incluido: Redirección desde el botón de pago hacia la plataforma PayPal y retorno al sistema tras el procesamiento.

3 Criterios de aceptación:

    * El botón de pago debe redirigir correctamente a la página de PayPal.
    * Los datos del pago deben ser transmitidos correctamente a PayPal.
    * Tras completar el pago, el usuario debe regresar al sistema con el estado del pago actualizado.
    * En caso de error, se debe mostrar un mensaje claro en la interfaz.

4 Casos de prueba

    * ID de prueba: PUI-001
    * Descripción: Validar la redirección a PayPal desde el sistema.
    * Precondiciones: El sistema debe estar configurado con las credenciales de PayPal.
    * Pasos a seguir:
        1- Acceder a la página del pedido.
        2- Seleccionar la opción de pago con PayPal.
        3- Confirmar el pago en la página de PayPal.
        4- Volver al sistema tras completar el proceso.
    * Resultado esperado: El usuario es redirigido correctamente y el estado del pago se actualiza a exitoso o fallido según la respuesta de PayPal.
    * Resultado real:
    * Observaciones: N/A
    * Aprobación: Negada/Aprobada

-----------------------------------

Prueba de interfaz de usuario: Formulario de autenticación en Mercado Libre

1 Introducción

    * Propósito: Validar que el formulario de autenticación para procesar pagos con Mercado Libre sea funcional y permita gestionar correctamente los tokens de acceso.

2 Alcance

    * Incluido: Interacción del usuario con el formulario de autenticación para Mercado Libre.

3 Criterios de aceptación:

    * El formulario debe permitir ingresar credenciales válidas.
    * Tras la autenticación, el sistema debe recibir el token de acceso válido.
    * En caso de error, se debe mostrar un mensaje claro y permitir reintentar.
    * El formulario debe cumplir con estándares de usabilidad.

4 Casos de prueba

    * ID de prueba: PUI-002
    * Descripción: Validar el funcionamiento del formulario de autenticación con Mercado Libre.
    * Precondiciones: El sistema debe estar configurado con acceso al API de Mercado Libre.
    * Pasos a seguir:
        1- Iniciar sesión en el sistema.
        2- Acceder a un pedido y seleccionar pago con Mercado Libre.
        3- Ingresar credenciales en el formulario de autenticación.
        4- Confirmar el pago y verificar el estado en el sistema.
    * Resultado esperado: El usuario puede autenticarse correctamente y el pago se procesa con éxito.
    * Resultado real:
    * Observaciones: N/A
    * Aprobación: Negada/Aprobada

    
---------------------------------------------------------------------------

Prueba de interfaz de usuario: Selección del método de pago

1 Introducción

    * Propósito: Validar que el usuario pueda seleccionar correctamente entre los métodos de pago disponibles (PayPal o Mercado Libre) en la interfaz del sistema.

2 Alcance

    * Incluido: Visualización y selección de métodos de pago en la página del pedido.

3 Criterios de aceptación:

    * Los métodos de pago deben mostrarse claramente en la interfaz.
    * La selección de un método debe activar el flujo correspondiente (PayPal o Mercado Libre).
    * En caso de selección errónea, se debe mostrar un mensaje claro para el usuario.
    * El diseño debe ser responsivo y funcional en dispositivos móviles y de escritorio.

4Casos de prueba

    * ID de prueba: PUI-003
    * Descripción: Validar que el usuario pueda elegir y activar el flujo del método de pago deseado.
    * Precondiciones: El sistema debe estar configurado con ambos métodos de pago activos.
    * Pasos a seguir:
        1- Acceder a la página del pedido.
        2- Visualizar los métodos de pago disponibles.
        3- Seleccionar "PayPal" y verificar que redirija correctamente al flujo correspondiente.
        4- Repetir el proceso seleccionando "Mercado Libre".
    * Resultado esperado: El sistema activa el flujo correspondiente según el método de pago seleccionado.
    * Resultado real:
    * Observaciones: N/A
    * Aprobación: Negada/Aprobada


Prueba de interfaz de usuario: Mensaje de error por datos incompletos

1   Introducción

    *Propósito: Validar que el sistema muestre un mensaje de error claro si el usuario intenta procesar un pago sin ingresar todos los datos necesarios.

2   Alcance

    * Incluido: Validación de campos obligatorios en la interfaz al procesar un pago.

3   Criterios de aceptación:

    * Si faltan datos requeridos, el sistema debe mostrar un mensaje de error claro e indicar qué datos faltan.
    * El usuario no debe poder continuar hasta completar los campos requeridos.
    * El diseño del mensaje de error debe ser accesible y fácil de entender.

4   Casos de prueba

    * ID de prueba: PUI-004
    * Descripción: Verificar el mensaje de error cuando faltan datos obligatorios para procesar el pago.
    * Precondiciones: El sistema debe estar configurado para validar campos obligatorios.
    * Pasos a seguir:
        1- Acceder a la página de pago.
        2- Seleccionar un método de pago.
        3- Intentar procesar el pago sin ingresar el monto o seleccionar un método.
        4- Resultado esperado: Aparece un mensaje de error indicando los campos faltantes y el pago no se procesa.
    * Resultado real:
    * Observaciones: N/A
    * Aprobación: Negada/Aprobada


"""

