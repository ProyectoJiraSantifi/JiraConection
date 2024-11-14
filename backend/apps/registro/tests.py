"""
Prueba de unidad: Módulo Registro de Usuario.

1. Introducción
   - Propósito: Validar que el módulo de registro de usuario funcione correctamente y 
   cumpla con los requisitos establecidos para el registro exitoso.

2. Alcance
   - Incluido: Registro de nuevos usuarios y validación de datos.

3. Criterios de aceptación:
   - El sistema debe aceptar un email y una contraseña válidos.
   - El registro debe completarse correctamente al confirmar el email.
   - Debe mostrar mensajes de error claros cuando no se cumplan los requisitos.
   - El usuario debe ser capaz de iniciar sesión después del registro exitoso.

4. Casos de prueba:

- ID de prueba: U-001
    - Descripción: Verificar que el sistema acepte un email y una contraseña válidos para el registro.
    - Precondiciones: El usuario accede a la vista de registro.
    - Pasos a seguir:
        1. Ingresar un email válido y una contraseña válida en los campos de registro.
        2. Hacer clic en "Registrar".
    - Resultado esperado: Registro exitoso y mensaje de confirmación enviado al email del usuario.
    - Resultado real: <Resultado de la operación>
    - Observaciones: N/A
    - Aprobación: Negada - Aprobada


- ID de prueba: U-002
    - Descripción: Verificar que el sistema muestre un mensaje de error si el email no es válido.
    - Precondiciones: El usuario accede a la vista de registro.
    - Pasos a seguir:
        1. Ingresar un email no válido y una contraseña válida.
        2. Hacer clic en "Registrar".
    - Resultado esperado: Mensaje de error indicando que el email es inválido.
    - Resultado real: <Resultado de la operación>
    - Observaciones: N/A
    - Aprobación: Negada - Aprobada


- ID de prueba: U-003
    - Descripción: Verificar que el sistema requiera que ambos campos, email y contraseña, estén llenos antes de registrar al usuario.
    - Precondiciones: El usuario accede a la vista de registro.
    - Pasos a seguir:
        1. Dejar vacío el campo de email o contraseña.
        2. Hacer clic en "Registrar".
    - Resultado esperado: Mensaje de error indicando que ambos campos deben completarse.
    - Resultado real: <Resultado de la operación>
    - Observaciones: N/A
    - Aprobación: Negada - Aprobada


- ID de prueba: U-004
    - Descripción: Verificar que el sistema envíe un correo de confirmación al email proporcionado por el usuario.
    - Precondiciones: El usuario accede a la vista de registro y proporciona un email válido.
    - Pasos a seguir:
        1. Ingresar un email y una contraseña válidos.
        2. Hacer clic en "Registrar".
    - Resultado esperado: El sistema envía un correo de confirmación al email ingresado.
    - Resultado real: <Resultado de la operación>
    - Observaciones: N/A
    - Aprobación: Negada - Aprobada

- ID de prueba: U-005
    - Descripción: Verificar que el usuario no pueda registrarse con un email ya existente en el sistema.
    - Precondiciones: El usuario intenta registrarse con un email ya registrado.
    - Pasos a seguir:
        1. Ingresar un email ya existente y una contraseña.
        2. Hacer clic en "Registrar".
    - Resultado esperado: Mensaje de error indicando que el email ya está registrado.
    - Resultado real: <Resultado de la operación>
    - Observaciones: N/A
    - Aprobación: Negada - Aprobada
"""

# -------------------------------------------------------------

"""
Prueba de Rendimiento: Inicio de Sesión Seguro

1. Introducción
   - Propósito: Evaluar el rendimiento del sistema de inicio de sesión seguro bajo diferentes cargas y condiciones de red para asegurar la experiencia del usuario en el acceso al sistema.

2. Alcance
   - Incluido: Módulo de Inicio de Sesión Seguro

3. Criterios de aceptación:
   - Tiempo de respuesta en menos de 2 segundos bajo carga.
   - Manejo adecuado de errores y mensajes claros en caso de fallos.
   - Rendimiento consistente tanto en la autenticación mediante email y contraseña como con Google.

4. Casos de prueba:

- Prueba 1
    - ID de prueba: PR-001
    - Descripción: Evaluar el tiempo de respuesta al iniciar sesión con 1000 usuarios simultáneos.
    - Precondiciones: Sistema en producción; base de datos operativa.
    - Cargas de prueba: 1000 usuarios simultáneos.
    - Pasos a seguir:
        - 1. Simular el acceso de 1000 usuarios a la vista de inicio de sesión.
        - 2. Cada usuario ingresa sus credenciales de email y contraseña.
        - 3. Medir el tiempo de respuesta del sistema.
    - Resultado esperado: Respuesta en menos de 2 segundos por solicitud.
    - Resultado real: <Resultado de la operación>
    - Observaciones: N/A
    - Aprobación: Negada - Aprobada

- Prueba 2
    - ID de prueba: PR-002
    - Descripción: Evaluar el tiempo de respuesta para usuarios que acceden con Google bajo una conexión de baja velocidad (256 kbps).
    - Precondiciones: Sistema en producción; cuenta de Google válida.
    - Cargas de prueba: 500 usuarios con conexión de baja velocidad.
    - Pasos a seguir:
        - 1. Configurar 500 usuarios con conexión simulada de baja velocidad.
        - 2. Cada usuario intenta iniciar sesión usando la opción de Google.
        - 3. Medir el tiempo de respuesta del sistema.
    - Resultado esperado: Inicio de sesión en menos de 5 segundos por solicitud.
    - Resultado real: <Resultado de la operación>
    - Observaciones: N/A
    - Aprobación: Negada - Aprobada

- Prueba 3
    - ID de prueba: PR-003
    - Descripción: Verificar el manejo de 2000 intentos fallidos de inicio de sesión en un período de 5 minutos.
    - Precondiciones: Sistema en producción.
    - Cargas de prueba: 2000 intentos fallidos.
    - Pasos a seguir:
        - 1. Enviar 2000 intentos de inicio de sesión con credenciales incorrectas en un intervalo de 5 minutos.
        - 2. Observar la estabilidad del sistema y los mensajes de error.
    - Resultado esperado: Mensaje de error claro, sin impacto en el rendimiento general del sistema.
    - Resultado real: <Resultado de la operación>
    - Observaciones: N/A
    - Aprobación: Negada - Aprobada

- Prueba 4
    - ID de prueba: PR-004
    - Descripción: Evaluar el rendimiento del sistema con 5000 usuarios que intentan iniciar sesión en una hora.
    - Precondiciones: Sistema operativo y en alto rendimiento.
    - Cargas de prueba: 5000 usuarios en una hora.
    - Pasos a seguir:
        - 1. Distribuir la carga para enviar 5000 solicitudes de inicio de sesión durante una hora.
        - 2. Monitorear la estabilidad del sistema y medir el tiempo de respuesta.
    - Resultado esperado: Tiempo de respuesta menor a 2 segundos sin caídas del sistema.
    - Resultado real: <Resultado de la operación>
    - Observaciones: N/A
    - Aprobación: Negada - Aprobada

- Prueba 5
    - ID de prueba: PR-005
    - Descripción: Verificar el proceso de inicio de sesión cuando la red se interrumpe a mitad del proceso de autenticación.
    - Precondiciones: Sistema operativo y red accesible.
    - Cargas de prueba: 500 usuarios con interrupción de red.
    - Pasos a seguir:
        - 1. Iniciar sesión para 500 usuarios.
        - 2. Interrumpir la conexión de red a mitad del proceso de autenticación.
        - 3. Reconectar y verificar si el sistema retoma el proceso o solicita iniciar sesión nuevamente.
    - Resultado esperado: El sistema muestra un mensaje de reconexión clara o solicita repetir el inicio de sesión.
    - Resultado real: <Resultado de la operación>
    - Observaciones: N/A
    - Aprobación: Negada - Aprobada
"""
