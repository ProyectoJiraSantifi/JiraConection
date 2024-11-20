"""
Pruebas de Integración: Producto - Inventario

1. Introducción
    Propósito: Verificar la integración entre la clase Producto y el módulo Inventario, asegurando que las operaciones de 
    administración del inventario (agregar, eliminar, actualizar y consultar productos) se ejecuten correctamente, cumpliendo con los 
    requisitos funcionales esperados.

2. Alcance
    Incluido:
        - Módulo Inventario.
        - Clase Producto.
        - Métodos: agregarProducto, eliminarProducto, actualizarProducto, obtenerDetalles.

3. Criterios de aceptación
    - Los productos deben agregarse correctamente al inventario.
    - Los productos pueden eliminarse del inventario sin afectar otros datos.
    - Las actualizaciones deben reflejarse únicamente en los productos modificados.
    - La consulta por ID debe devolver el producto correcto o manejar correctamente un error si el producto no existe.
    - El inventario debe manejar múltiples productos sin errores o inconsistencias.

4. Casos de prueba

    - ID de prueba: PI-001
        - Descripción: Verificar que se agrega un producto al inventario.
        - Precondiciones:
            - Módulos Producto e Inventario compilados.
            - Lista productos vacía en el inventario.
        - Pasos a seguir:
            1. Crear una instancia del inventario.
            2. Crear un nuevo producto con atributos válidos.
            3. Usar el método agregarProducto para añadir el producto al inventario.
            4. Verificar que el producto está presente en la lista productos del inventario.
        - Resultado esperado: El producto aparece correctamente en el inventario.
        - Resultado real: El producto fue añadido exitosamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-002
        - Descripción: Verificar que se elimina un producto del inventario.
        - Precondiciones:
            - Módulos Producto e Inventario compilados.
            - La lista productos contiene al menos un producto.
        - Pasos a seguir:
            1. Crear una instancia del inventario con al menos un producto.
            2. Usar el método eliminarProducto para remover el producto.
            3. Verificar que el producto ya no está en la lista productos.
        - Resultado esperado: El producto es eliminado correctamente.
        - Resultado real: El producto fue eliminado exitosamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-003
        - Descripción: Verificar que se actualiza la información de un producto en el inventario.
        - Precondiciones:
            - Módulos Producto e Inventario compilados.
            - La lista productos contiene al menos un producto.
        - Pasos a seguir:
            1. Crear una instancia del inventario con al menos un producto.
            2. Usar el método actualizarProducto para cambiar el stock o precio del producto.
            3. Verificar que el producto tiene la información actualizada.
        - Resultado esperado: El producto se actualiza correctamente.
        - Resultado real: El producto fue actualizado exitosamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-004
        - Descripción: Verificar la administración de múltiples productos en el inventario.
        - Precondiciones:
            - Módulos Producto e Inventario compilados.
            - Lista productos inicialmente vacía.
        - Pasos a seguir:
            1. Crear una instancia del inventario.
            2. Agregar al menos tres productos con atributos distintos.
            3. Actualizar el stock de un producto específico.
            4. Verificar que solo ese producto se haya actualizado.
        - Resultado esperado: El inventario maneja múltiples productos y las actualizaciones son específicas.
        - Resultado real: Los productos fueron gestionados exitosamente y las actualizaciones fueron específicas.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-005
        - Descripción: Verificar la recuperación de un producto específico desde el inventario.
        - Precondiciones:
            - Módulos Producto e Inventario compilados.
            - La lista productos contiene al menos dos productos.
        - Pasos a seguir:
            1. Crear una instancia del inventario con al menos dos productos.
            2. Llamar al método obtenerDetalles con un idProducto existente.
            3. Verificar que la información retornada corresponde al producto buscado.
            4. Repetir el procedimiento con un idProducto inexistente y verificar el manejo del error.
        - Resultado esperado: La información del producto se obtiene correctamente o se gestiona adecuadamente si no existe.
        - Resultado real: La información del producto fue obtenida correctamente, y el sistema manejó correctamente el idProducto inexistente.
        - Observaciones: N/A
        - Aprobación: Aprobada
"""
