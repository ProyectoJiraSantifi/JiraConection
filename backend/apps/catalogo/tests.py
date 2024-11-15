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