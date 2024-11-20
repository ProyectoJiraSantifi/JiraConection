
"""
Prueba de unidad: Módulo Filtrar Pedidos Anteriores.

1. Introducción.
    Propósito: El propósito de estas pruebas es validar que la funcionalidad de filtrado de pedidos anteriores funcione correctamente según los criterios de filtrado especificados.

2. Alcance.
    Incluido: Filtrado de pedidos por fecha, estado del pedido, y otros parámetros definidos.

3. Criterios de aceptación:
    - El sistema debe permitir filtrar pedidos por fecha.
    - El sistema debe permitir filtrar pedidos por estado (Ejemplo: "Enviado", "Pendiente").
    - Los filtros deben mostrar resultados correctos según los criterios seleccionados.
    - Los resultados filtrados deben ser presentados de manera correcta y clara.

4. Casos de prueba.

    - ID de prueba: U-001

    - Descripción: Verificar que el sistema filtre los pedidos correctamente por fecha.

    - Precondiciones: El usuario debe haber realizado varios pedidos en diferentes fechas.

    Pasos a seguir:
    1. Iniciar sesión con el usuario.
    2. Acceder al historial de compras.
    3. Aplicar el filtro por fecha.
    4. Verificar que los resultados correspondan a las fechas seleccionadas.
    
    Resultado esperado: Los pedidos deben ser filtrados correctamente por fecha y mostrados en el historial.

    Resultado real: Los pedidos fueron filtrados correctamente por fecha.

    Observaciones: N/A

    Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: U-002

    - Descripción: Verificar que el sistema filtre los pedidos correctamente por estado.

    - Precondiciones: El usuario debe haber realizado varios pedidos con distintos estados (Ejemplo: "Enviado", "Pendiente").

    Pasos a seguir:
    1. Iniciar sesión con el usuario.
    2. Acceder al historial de compras.
    3. Aplicar el filtro por estado del pedido.
    4. Verificar que los resultados corresponden al estado seleccionado.
    
    Resultado esperado: Los pedidos deben ser filtrados correctamente según el estado (Ejemplo: "Enviado", "Pendiente").

    Resultado real: Los pedidos fueron filtrados correctamente por estado.

    Observaciones: N/A

    Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: U-003

    - Descripción: Verificar que el sistema muestre un mensaje adecuado cuando no se encuentren pedidos con los filtros aplicados.

    - Precondiciones: El usuario debe haber realizado pedidos que no coincidan con los criterios de filtrado.

    Pasos a seguir:
    1. Iniciar sesión con el usuario.
    2. Acceder al historial de compras.
    3. Aplicar un filtro que no coincida con los pedidos (por ejemplo, filtrar por estado "Cancelado" cuando no se haya hecho ningún pedido cancelado).
    4. Verificar que se muestre un mensaje indicando que no se encontraron resultados.
    
    Resultado esperado: El sistema debe mostrar un mensaje indicando que no se encontraron resultados para el filtro aplicado.

    Resultado real: El mensaje de "No se encontraron resultados" fue mostrado correctamente.

    Observaciones: N/A

    Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: U-004

    - Descripción: Verificar que el sistema filtre los pedidos correctamente por un rango de fechas.

    - Precondiciones: El usuario debe haber realizado pedidos en varias fechas.

    Pasos a seguir:
    1. Iniciar sesión con el usuario.
    2. Acceder al historial de compras.
    3. Aplicar un filtro por rango de fechas (por ejemplo, seleccionar una fecha de inicio y una fecha de fin).
    4. Verificar que los pedidos mostrados estén dentro del rango de fechas seleccionado.

    Resultado esperado: Los pedidos deben ser filtrados correctamente dentro del rango de fechas seleccionado.

    Resultado real: Los pedidos fueron filtrados correctamente por el rango de fechas.

    Observaciones: N/A

    Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: U-005

    - Descripción: Verificar que el sistema permita filtrar pedidos por múltiples criterios simultáneamente (fecha y estado).

    - Precondiciones: El usuario debe haber realizado pedidos en varias fechas y con diferentes estados.

    Pasos a seguir:
    1. Iniciar sesión con el usuario.
    2. Acceder al historial de compras.
    3. Aplicar los filtros de fecha y estado simultáneamente.
    4. Verificar que los resultados filtrados coincidan con ambos criterios (fecha y estado).

    Resultado esperado: Los pedidos deben ser filtrados correctamente por ambos criterios simultáneamente.

    Resultado real: Los pedidos fueron filtrados correctamente por fecha y estado.

    Observaciones: N/A

    Aprobación: Aprobada
"""


"""
Prueba funcional: Módulo Registro y Gestión de Pedidos

1. Introducción.
    Propósito: El propósito de estas pruebas es validar que el módulo de registro de usuarios y la gestión de pedidos (historial, 
    filtrado y detalles de pedidos) funcionen correctamente según las especificaciones proporcionadas.

2. Alcance.
    Incluido:
        - Registro de usuarios.
        - Visualización y filtrado de pedidos.
        - Consulta de historial de compras.

3. Criterios de aceptación:
    - El usuario debe poder registrarse correctamente.
    - El usuario debe poder ver y filtrar sus pedidos según diferentes criterios.
    - El usuario debe poder ver detalles específicos de un pedido.
    - El historial de compras debe actualizarse correctamente con los pedidos realizados por el usuario.

4. Casos de prueba.

    - ID de prueba: PFU-001
        - Descripción: Realizar el registro de un usuario.
        - Precondiciones: Ninguna.
        
        Pasos a seguir:
        1. Ingresar los datos del usuario (nombre, correo, contraseña, dirección).
        2. Hacer clic en el botón de registro.
        
        Resultado esperado: El usuario debe ser registrado correctamente.
        Resultado real: El usuario fue registrado exitosamente.
        Observaciones: N/A
        Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: PFU-002
        - Descripción: Ver el historial de compras de un usuario.
        - Precondiciones: El usuario debe estar registrado y haber realizado al menos una compra.
        
        Pasos a seguir:
        1. Iniciar sesión con el usuario.
        2. Acceder al historial de compras.
        
        Resultado esperado: El historial de compras debe mostrar todos los pedidos realizados por el usuario.
        Resultado real: El historial de compras fue mostrado correctamente.
        Observaciones: N/A
        Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: PFU-003
        - Descripción: Filtrar el historial de compras por fecha de compra.
        - Precondiciones: El usuario debe haber realizado múltiples compras en diferentes fechas.
        
        Pasos a seguir:
        1. Iniciar sesión con el usuario.
        2. Acceder al historial de compras.
        3. Aplicar el filtro por fecha de compra.
        4. Verificar que los resultados filtrados sean correctos.
        
        Resultado esperado: Los pedidos deben mostrarse correctamente dentro del rango de fechas seleccionado.
        Resultado real: El historial fue filtrado correctamente por fecha.
        Observaciones: N/A
        Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: PFU-004
        - Descripción: Ver los detalles de un pedido específico.
        - Precondiciones: El usuario debe haber realizado al menos un pedido.
        
        Pasos a seguir:
        1. Iniciar sesión con el usuario.
        2. Acceder al historial de compras.
        3. Seleccionar un pedido específico para ver más detalles.
        
        Resultado esperado: El detalle del pedido debe mostrar toda la información del pedido, incluidos los productos, precio total y estado del pedido.
        Resultado real: El detalle del pedido fue mostrado correctamente.
        Observaciones: N/A
        Aprobación: Aprobada

    -------------------------------------

    - ID de prueba: PFU-005
        - Descripción: Filtrar los pedidos por estado (Ejemplo: "Enviado", "Pendiente").
        - Precondiciones: El usuario debe haber realizado varios pedidos con distintos estados.
        
        Pasos a seguir:
        1. Iniciar sesión con el usuario.
        2. Acceder al historial de compras.
        3. Aplicar el filtro por estado del pedido.
        4. Verificar que los resultados filtrados sean correctos según el estado seleccionado.
        
        Resultado esperado: Los pedidos deben filtrarse y mostrarse correctamente según el estado seleccionado (Ejemplo: "Enviado").
        Resultado real: Los pedidos fueron filtrados correctamente por estado.
        Observaciones: N/A
        Aprobación: Aprobada
"""
