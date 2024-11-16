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

----------------------------------------------------------

Prueba 5: Seguridad en el Procesamiento de Tarjetas Bancarias

Introducción
Propósito: Verificar que el sistema maneje de forma segura la información de tarjetas bancarias y cumpla con los estándares PCI DSS.

Alcance
Incluido:

Validación de datos de tarjetas
Encriptación de información sensible
Enmascaramiento de números de tarjeta
Validación de fecha de expiración y CVV

Excluido:

Procesamiento real de transacciones bancarias
Conexiones con redes bancarias externas

Criterios de aceptación:
Los números de tarjeta deben estar encriptados en tránsito y en reposo
Solo se deben mostrar los últimos 4 dígitos de la tarjeta
El CVV nunca debe ser almacenado
La información sensible debe ser eliminada después del procesamiento

Casos de prueba

ID de prueba: SEG-005
Descripción: Validar el manejo seguro de datos de tarjetas bancarias.
Precondiciones: Sistema configurado con encriptación TLS 1.2 o superior.
Pasos a seguir:

Ingresar datos de una tarjeta de prueba
Verificar la encriptación durante la transmisión
Verificar el enmascaramiento en la interfaz
Intentar acceder a los datos sin autorización
Verificar logs del sistema por exposición de datos sensibles

Resultado esperado:

Datos transmitidos de forma encriptada
Número de tarjeta enmascarado en todas las interfaces
CVV no almacenado en base de datos
Acceso denegado a intentos no autorizados
Logs limpios de información sensible

Resultado real:
Observaciones: N/A
Aprobación: Aprobada/Negada

----------------------------------------------------------

Prueba 6: Integridad y Eliminación Segura de Datos

Introducción
Propósito: Asegurar que la información sensible de pagos no persista en el sistema más allá del tiempo necesario para el procesamiento.

Alcance
Incluido:
Proceso de eliminación segura de datos
Verificación de datos residuales
Validación de logs y cachés

Excluido:
Backups del sistema
Datos archivados históricos

Criterios de aceptación:
La información sensible debe ser eliminada inmediatamente después del procesamiento
No deben quedar rastros en caché o archivos temporales
Los logs no deben contener información sensible
Debe existir un registro de la eliminación exitosa

Casos de prueba
ID de prueba: SEG-006
Descripción: Verificar la eliminación segura de datos sensibles post-procesamiento.
Precondiciones: Sistema con transacciones procesadas que contengan datos sensibles.
Pasos a seguir:

Procesar un pago con tarjeta de prueba
Verificar el procesamiento exitoso
Revisar todas las ubicaciones posibles de almacenamiento:

Base de datos principal
Archivos temporales
Logs del sistema
Caché de aplicación


Intentar recuperar los datos eliminados
Verificar registros de auditoría

Resultado esperado:

Datos sensibles completamente eliminados
Sin información recuperable en ningún almacenamiento
Registro de auditoría que confirme la eliminación
Imposibilidad de acceder a los datos eliminados

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


--------------------------------------------------


1  Introducción

    * Propósito: Garantizar la protección de datos sensibles, la validación de entradas y la gestión segura de la comunicación con plataformas externas como PayPal y Mercado Libre, previniendo accesos no autorizados o manipulación de datos en el sistema.

2 Alcance

    * Incluido:
        * Manejo seguro de tokens y credenciales de PayPal y Mercado Libre.
        * Validación de datos enviados a los métodos procesarPago() y verificarPago().
        * Protección de la relación uno a uno entre Pedido y Pago.
    * Excluido: Seguridad interna de las plataformas externas (PayPal y Mercado Libre).

3   Criterios de aceptación:

    * Los tokens y credenciales deben estar cifrados tanto en tránsito como en reposo.
    * El sistema debe validar todas las entradas antes de procesar un pago.
    * Ningún usuario no autenticado o no autorizado debe poder modificar datos de un pago o su estado.
    * Las conexiones con las APIs externas deben ser seguras (por ejemplo, HTTPS).
    * En caso de error, el sistema no debe exponer datos técnicos ni información sensible.

    
----------------------------------------------------------------------------------------

Prueba de seguridad: Validación de datos enviados a plataformas externas

1   Introducción

    * Propósito: Garantizar que los datos transmitidos a PayPal y Mercado Libre sean validados y protegidos contra inyección de datos maliciosos.

2   Alcance

    * Incluido: Validación de los datos enviados a las plataformas externas.
    * Excluido: Fallos de seguridad inherentes a las plataformas externas.

3   Criterios de aceptación:

    * Los datos enviados deben cumplir con los formatos requeridos por las plataformas.
    * Cualquier dato sospechoso debe ser rechazado antes de enviarse.
    * Las conexiones a las plataformas externas deben ser cifradas (HTTPS).
    * Los registros deben incluir cualquier intento de inyección o manipulación de datos.

3   Casos de prueba

    * ID de prueba: PS-001
    * Descripción: Verificar que los datos enviados no contengan valores maliciosos.
    * Precondiciones: El sistema debe estar configurado para conectarse a las plataformas de pago.
    * Pasos a seguir:
        1- Ingresar valores maliciosos en los campos del formulario (por ejemplo, scripts o consultas SQL).
        2- Intentar procesar un pago con PayPal y Mercado Libre.
        3- Verificar que los datos maliciosos sean rechazados antes de enviarse.
    * Resultado esperado: Los datos maliciosos son detectados y bloqueados, el sistema muestra un mensaje de error.
    * Resultado real:
    * Observaciones: N/A
    * Aprobación: Negada/Aprobada

-----------------------------------------------------------------------------------------

2 Prueba de seguridad: Gestión de tokens en Mercado Libre

1-  Introducción

*   Propósito: Validar que los tokens generados para la conexión con la API de Mercado Libre estén protegidos contra ataques como interceptación y reutilización.

2-  Alcance

*   Incluido: Generación, almacenamiento y uso de tokens de autenticación.
* Excluido: Seguridad del sistema externo de Mercado Libre.

3-  Criterios de aceptación:

    * Los tokens deben generarse utilizando métodos seguros y expirar tras un periodo definido.
    * Los tokens no deben almacenarse en texto plano.
    * La reutilización de tokens caducados debe ser rechazada.
    * Las conexiones deben ser seguras (TLS 1.2 o superior).

4 Casos de prueba

    * ID de prueba: PS-002
    * Descripción: Validar la seguridad en la gestión de tokens para Mercado Libre.
    * Precondiciones: El sistema debe estar configurado con acceso al API de Mercado Libre.
    * Pasos a seguir:
        1- Realizar un pago utilizando un token válido.
        2- Intentar reutilizar el mismo token para una segunda transacción.
        3- Interceptar la solicitud y analizar si el token está cifrado.

    * Resultado esperado: El sistema rechaza la reutilización de tokens y protege los tokens en tránsito.
    * Resultado real:
    * Observaciones: N/A
    * Aprobación: Negada/Aprobada

-------------------------------------------------------------------------------------------

3 Prueba de seguridad: Protección contra ataques de fuerza bruta en autenticación

1 Introducción

    * Propósito: Garantizar que el sistema proteja las interfaces de autenticación frente a ataques de fuerza bruta.

2 Alcance

    * Incluido: Intentos de acceso no autorizados a través de la autenticación para PayPal y Mercado Libre.
    * Excluido: Ataques directos a las plataformas externas.

3 Criterios de aceptación:

    * El sistema debe bloquear la cuenta tras múltiples intentos fallidos de autenticación.
    * Los intentos fallidos deben registrarse en los logs de seguridad.
    * Debe mostrarse un mensaje claro al usuario tras el bloqueo.
    * El bloqueo debe liberarse solo mediante procedimientos seguros.

4 Casos de prueba

    * ID de prueba: PS-003
    * Descripción: Validar el comportamiento del sistema ante intentos repetidos de autenticación fallida.
    * Precondiciones: La autenticación debe estar configurada para ambas plataformas.
    * Pasos a seguir:
        1- Intentar autenticarse con credenciales incorrectas más de cinco veces.
        2- Verificar que el sistema bloquee el acceso tras múltiples intentos.
        3- Intentar desbloquear mediante procedimientos no autorizados.
    * Resultado esperado: El acceso es bloqueado tras múltiples intentos fallidos y se registran los eventos.
    * Resultado real:
    * Observaciones: N/A
    * Aprobación: Negada/Aprobada

---------------------------------------------------------------------------------------------

Prueba de seguridad: Cifrado de datos sensibles

1-  Introducción

    * Propósito: Validar que los datos sensibles como el idPago, el monto y los datos de usuario estén cifrados durante su transmisión y almacenamiento.

2-  Alcance

    * Incluido: Cifrado de datos sensibles en tránsito y reposo.
    * Excluido: Análisis de cifrado en plataformas externas.

3-  Criterios de aceptación:

    * Los datos sensibles deben cifrarse utilizando estándares modernos (AES-256, TLS 1.2 o superior).
    * Los datos almacenados en la base de datos deben estar cifrados y no ser accesibles directamente.
    * Los logs del sistema no deben contener datos sensibles en texto plano.
    * El acceso a datos cifrados debe estar restringido por permisos adecuados.

4-  Casos de prueba

    * ID de prueba: PS-004
    * Descripción: Verificar que los datos sensibles estén cifrados en todas las etapas del proceso.
    * Precondiciones: El sistema debe estar configurado con métodos de cifrado.
    * Pasos a seguir:
        1- Realizar un pago y capturar la transmisión de datos para verificar el cifrado.
        2- Inspeccionar la base de datos y los logs para confirmar que los datos sensibles no estén en texto plano.
        3- Intentar acceder a los datos cifrados sin las credenciales necesarias.
    * Resultado esperado: Todos los datos sensibles están cifrados y protegidos contra accesos no autorizados.
    * Resultado real:
    * Observaciones: N/A
    * Aprobación: Negada/Aprobada


"""

