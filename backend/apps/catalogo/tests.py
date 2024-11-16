"""
Prueba funcional: Filtro de productos

1. Introducción.
   - Propósito: Validar que el sistema de filtrado de productos funcione correctamente y 
   permita a los usuarios encontrar productos específicos según sus preferencias.

2. Alcance.
   - Incluido: Filtrado de productos por categoría y precio en el catálogo.

3. Criterios de aceptación:
   - El sistema debe mostrar solo los productos que cumplan con el filtro seleccionado.
   - Los filtros deben aplicarse en menos de 2 segundos.
   - En caso de error, el sistema debe mostrar un mensaje claro al usuario.
   - El sistema debe permitir aplicar múltiples filtros de forma simultánea.

4. Casos de prueba:

    - Prueba 1
        - ID de prueba: PFU-001
        - Descripción: Verificar el filtrado por categoría.
        - Precondiciones: El usuario tiene acceso al catálogo de productos.
    - Pasos a seguir:
            1. Seleccionar una categoría específica (por ejemplo, "Electrónica").
            2. Observar los productos desplegados.
        - Resultado esperado: Solo se muestran productos de la categoría "Electrónica".
        - Resultado real: Productos de la categoría "Electrónica" se muestran correctamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

-------------------------------------

    - Prueba 2
        - ID de prueba: PFU-002
        - Descripción: Verificar el filtrado por rango de precio.
        - Precondiciones: El usuario tiene acceso al catálogo de productos.
        - Pasos a seguir:
            1. Seleccionar un rango de precios (por ejemplo, de $50 a $100).
            2. Observar los productos desplegados.
        - Resultado esperado: Solo se muestran productos cuyo precio esté entre $50 y $100.
        - Resultado real: Productos dentro del rango de $50 a $100 se despliegan correctamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

-------------------------------------

    - Prueba 3
        - ID de prueba: PFU-003
        - Descripción: Verificar la combinación de filtros de categoría y precio.
        - Precondiciones: El usuario tiene acceso al catálogo de productos.
        - Pasos a seguir:
            1. Seleccionar la categoría "Electrónica".
            2. Establecer un rango de precios de $100 a $200.
            3. Observar los productos desplegados.
        - Resultado esperado: Solo se muestran productos de "Electrónica" con precios entre $100 y $200.
        - Resultado real: Se muestran productos de "Electrónica" dentro del rango de $100 a $200 correctamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

-------------------------------------

    - Prueba 4
        - ID de prueba: PFU-004
        - Descripción: Verificar el mensaje de error si no hay productos que cumplan con el filtro.
        - Precondiciones: El usuario tiene acceso al catálogo de productos.
        - Pasos a seguir:
            1. Seleccionar una categoría sin productos disponibles.
            2. Observar la respuesta del sistema.
        - Resultado esperado: El sistema muestra un mensaje indicando que no hay productos disponibles para el filtro seleccionado.
        - Resultado real: El sistema despliega mensaje: "No hay productos disponibles para esta categoría."
        - Observaciones: N/A
        - Aprobación: Aprobada

-------------------------------------

    - Prueba 5
        - ID de prueba: PFU-005
        - Descripción: Verificar el funcionamiento del sistema al seleccionar un rango de precios sin productos disponibles.
        - Precondiciones: El usuario tiene acceso al catálogo de productos.
        - Pasos a seguir:
            1. Seleccionar un rango de precios sin productos disponibles (por ejemplo, de $1000 a $2000).
            2. Observar la respuesta del sistema.
        - Resultado esperado: El sistema muestra un mensaje indicando que no hay productos disponibles en ese rango de precios.
        - Resultado real: El sistema despliega mensaje: "No hay productos disponibles en este rango de precios."
        - Observaciones: N/A
        - Aprobación: Negada (continúa la operación del sistema sin productos para mostrar)

-------------------------------------

Prueba funcional: Búsqueda de productos

1. Introducción.
   - Propósito: Validar que la búsqueda de productos funcione correctamente y que el usuario 
   pueda encontrar productos específicos mediante palabras clave.

2. Alcance.
   - Incluido: Búsqueda de productos por nombre y palabras clave.

3. Criterios de aceptación:
   - La búsqueda debe mostrar productos relevantes para las palabras clave ingresadas.
   - Los resultados de búsqueda deben aparecer en menos de 2 segundos.
   - En caso de error, se debe mostrar un mensaje claro al usuario.
   - El sistema debe permitir la búsqueda en todo el catálogo.

4. Casos de prueba:

    - Prueba 1
        - ID de prueba: PFU-006
        - Descripción: Verificar búsqueda por nombre de producto exacto.
        - Precondiciones: El usuario tiene acceso al catálogo de productos.
        - Pasos a seguir:
            1. Ingresar el nombre exacto de un producto (por ejemplo, "Smartphone").
            2. Observar los resultados de búsqueda.
        - Resultado esperado: El sistema muestra productos cuyo nombre coincide exactamente con "Smartphone".
        - Resultado real: Productos con nombre "Smartphone" aparecen correctamente en los resultados de búsqueda.
        - Observaciones: N/A
        - Aprobación: Aprobada

-------------------------------------

    - Prueba 2
        - ID de prueba: PFU-007
        - Descripción: Verificar búsqueda por palabras clave relacionadas (sinónimos o términos similares).
        - Precondiciones: El usuario tiene acceso al catálogo de productos.
        - Pasos a seguir:
            1. Ingresar una palabra clave relacionada (por ejemplo, "teléfono" para "Smartphone").
            2. Observar los resultados de búsqueda.
        - Resultado esperado: El sistema muestra productos relacionados con la palabra clave "teléfono".
        - Resultado real: Productos relacionados con "teléfono" se muestran correctamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

-------------------------------------

    - Prueba 3
        - ID de prueba: PFU-008
        - Descripción: Verificar búsqueda de productos con errores ortográficos leves en el nombre.
        - Precondiciones: El usuario tiene acceso al catálogo de productos.
        - Pasos a seguir:
            1. Ingresar una palabra clave con un error ortográfico leve (por ejemplo, "Smrtphone" en lugar de 
            "Smartphone").
            2. Observar los resultados de búsqueda.
        - Resultado esperado: El sistema muestra resultados relevantes a pesar del error ortográfico.
        - Resultado real: Productos similares a "Smartphone" se muestran correctamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

-------------------------------------

    - Prueba 4
        - ID de prueba: PFU-009
        - Descripción: Verificar que el sistema indique si no se encuentran resultados de búsqueda.
        - Precondiciones: El usuario tiene acceso al catálogo de productos.
        - Pasos a seguir:
            1. Ingresar un término de búsqueda sin resultados relevantes (por ejemplo, "Tablet XYZ").
            2. Observar la respuesta del sistema.
        - Resultado esperado: El sistema muestra un mensaje indicando que no se encontraron resultados para la búsqueda.
        - Resultado real: El sistema despliega mensaje: "No se encontraron resultados para la búsqueda."
        - Observaciones: N/A
        - Aprobación: Aprobada

-------------------------------------

    - Prueba 5
        - ID de prueba: PFU-010
        - Descripción: Verificar la búsqueda de productos con caracteres especiales en el nombre.
        - Precondiciones: El usuario tiene acceso al catálogo de productos.
        - Pasos a seguir:
            1. Ingresar un nombre de producto que contenga caracteres especiales (por ejemplo, "Cámara HD+").
            2. Observar los resultados de búsqueda.
        - Resultado esperado: El sistema muestra productos que contengan el nombre con caracteres especiales "Cámara HD+".
        - Resultado real: Productos con "Cámara HD+" se muestran correctamente en los resultados de búsqueda.
        - Observaciones: N/A
        - Aprobación: Aprobada
"""

"""
Prueba de visualicion de productos

    1. Introducción.
        Propósito: Verificar que el catálogo de productos se muestra correctamente con los detalles 
        esenciales (nombre, imagen, descripción, precio y disponibilidad) y que la barra de búsqueda y los filtros funcionan de manera efectiva.

    2. Alcance.
        Incluido: Visualización del catálogo de productos, funcionalidad de barra de búsqueda, filtros de categoría, precio y disponibilidad.

    3. Criterios de aceptación:
        - Los productos deben aparecer con la información completa (nombre, imagen, descripción, precio, disponibilidad).
        - La barra de búsqueda debe mostrar productos relacionados con el término ingresado.
        - Los filtros deben actualizar la lista de productos sin recargar la página.
        
    4. Casos de prueba.

        - ID de prueba: PUI-001

            - Descripción: Verificar que todos los productos registrados se muestren correctamente en el catálogo.

            - Precondiciones: El sistema tiene productos registrados.

            - Pasos a seguir:
                1. Acceder a la vista del catálogo de productos.
                2. Verificar que los productos se muestran con nombre, imagen, descripción, precio y disponibilidad.

            Resultado esperado: Los productos deben ser visibles con los detalles correctos.

            Resultado real: Todos los productos fueron mostrados correctamente, con la imagen, nombre, descripción, precio y disponibilidad bien definidos.

            Observaciones: No se presentaron errores en la carga de productos. La visualización fue clara y precisa.

            Aprobación: Aprobada

    -------------------------------------

        - ID de prueba: PUI-002

            - Descripción: Verificar el filtro por categoría.

            - Precondiciones: El sistema tiene productos en diferentes categorías.

            - Pasos a seguir:
                1. Aplicar un filtro por categoría específica.
                2. Verificar que solo los productos de la categoría seleccionada se muestren.

            Resultado esperado: Los productos deben actualizarse para mostrar solo los de la categoría seleccionada.

            Resultado real: El filtro de categoría funcionó correctamente y solo se mostraron los productos de la categoría seleccionada.

            Observaciones: La actualización de productos fue instantánea, sin necesidad de recargar la página.

            Aprobación: Aprobada

    -------------------------------------

        - ID de prueba: PUI-003

            - Descripción: Verificar el filtro por precio.

            - Precondiciones: El sistema tiene productos con diferentes rangos de precio.

            - Pasos a seguir:
                1. Aplicar el filtro de precio, seleccionando un rango específico.
                2. Verificar que solo los productos dentro del rango de precio seleccionado se muestren.

            Resultado esperado: Los productos deben actualizarse para mostrar solo los productos dentro del rango de precio seleccionado.

            Resultado real: El filtro de precio funcionó correctamente, mostrando solo los productos dentro del rango establecido.

            Observaciones: Los resultados se actualizaron rápidamente y los precios fueron mostrados claramente.

            Aprobación: Aprobada

    -------------------------------------

        - ID de prueba: PUI-004

            - Descripción: Verificar que la barra de búsqueda muestre productos que coincidan con el término de búsqueda.

            - Precondiciones: El sistema tiene productos con términos relevantes en nombre o descripción.

            - Pasos a seguir:
                1. Ingresar un término de búsqueda en la barra de búsqueda.
                2. Verificar que los productos que coincidan con el término ingresado aparezcan en la lista de resultados.

            Resultado esperado: Los productos que coincidan con el término de búsqueda deben aparecer en la lista de resultados.

            Resultado real: La barra de búsqueda mostró correctamente los productos relacionados con el término ingresado.

            Observaciones: La búsqueda fue rápida y precisa. Los resultados fueron relevantes.

            Aprobación: Aprobada

    -------------------------------------

        - ID de prueba: PUI-005

            - Descripción: Verificar que la disponibilidad de los productos esté correcta.

            - Precondiciones: El sistema tiene productos con diferentes estados de disponibilidad.

            - Pasos a seguir:
                1. Acceder a la vista del catálogo.
                2. Verificar que la disponibilidad (en stock o agotado) de cada producto sea correcta.

            Resultado esperado: La disponibilidad de los productos debe estar claramente visible y precisa.

            Resultado real: La disponibilidad de los productos fue correctamente mostrada como "en stock" o "agotado".

            Observaciones: Los productos agotados tenían una opción para notificación, lo cual mejoró la experiencia de usuario.

            Aprobación: Aprobada

"""
