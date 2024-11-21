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


"""
Pruebas de Integración Inversas: Inventario - Producto

1. Introducción
    Propósito: Validar que las instancias de la clase Producto puedan interactuar correctamente con el módulo Inventario, 
    cumpliendo con las funciones de consulta, actualización y manipulación de inventario.

2. Alcance
    Incluido:
        - Clase Producto.
        - Métodos del módulo Inventario: agregarProducto, eliminarProducto, actualizarProducto.

3. Criterios de aceptación
    - Un producto debe poder ser añadido correctamente al inventario.
    - Un producto debe poder ser eliminado del inventario en el que está contenido.
    - Las actualizaciones desde un producto deben reflejarse correctamente en el inventario.
    - La consulta desde un producto debe devolver los datos correctos del inventario.

4. Casos de prueba

    - ID de prueba: PI-INV-001
        - Descripción: Verificar que un producto puede añadirse a un inventario desde el punto de vista del producto.
        - Precondiciones:
            - Producto creado con atributos válidos.
            - Inventario inicializado con una lista vacía.
        - Pasos a seguir:
            1. Crear una instancia del inventario.
            2. Crear una instancia de Producto con atributos válidos.
            3. Usar el método agregarProducto del inventario para añadir el producto.
            4. Verificar que el producto pertenece al inventario.
        - Resultado esperado: El producto es añadido correctamente al inventario.
        - Resultado real: El producto fue añadido exitosamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-INV-002
        - Descripción: Verificar que un producto puede eliminarse del inventario desde el punto de vista del producto.
        - Precondiciones:
            - Producto añadido previamente al inventario.
        - Pasos a seguir:
            1. Crear una instancia del inventario con al menos un producto.
            2. Llamar al método eliminarProducto del inventario para eliminar el producto.
            3. Verificar que el producto ya no pertenece al inventario.
        - Resultado esperado: El producto es eliminado correctamente del inventario.
        - Resultado real: El producto fue eliminado exitosamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-INV-003
        - Descripción: Verificar que un producto puede solicitar que su stock sea actualizado en el inventario.
        - Precondiciones:
            - Producto existente en el inventario.
            - Stock inicial definido.
        - Pasos a seguir:
            1. Crear una instancia del inventario con un producto.
            2. Modificar el stock del producto usando actualizarProducto en el inventario.
            3. Verificar que el stock actualizado del producto se refleja en el inventario.
        - Resultado esperado: El stock del producto se actualiza correctamente en el inventario.
        - Resultado real: El stock fue actualizado exitosamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-INV-004
        - Descripción: Verificar que un producto puede obtener información sobre el inventario al que pertenece.
        - Precondiciones:
            - Producto existente en el inventario.
        - Pasos a seguir:
            1. Crear una instancia del inventario con un producto.
            2. Consultar la información del inventario desde el producto.
            3. Verificar que el inventario devuelto es el esperado.
        - Resultado esperado: El inventario al que pertenece el producto es identificado correctamente.
        - Resultado real: El inventario fue identificado correctamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-INV-005
        - Descripción: Verificar que un producto puede ser gestionado correctamente cuando forma parte de múltiples operaciones en el inventario.
        - Precondiciones:
            - Producto existente en el inventario.
        - Pasos a seguir:
            1. Crear una instancia del inventario con varios productos.
            2. Realizar múltiples operaciones (agregar, eliminar, actualizar) sobre el mismo producto.
            3. Verificar que las operaciones reflejan el estado correcto del producto en el inventario.
        - Resultado esperado: El producto se gestiona correctamente a través de múltiples operaciones.
        - Resultado real: El producto fue gestionado exitosamente en todas las operaciones.
        - Observaciones: N/A
        - Aprobación: Aprobada
"""

"""
Pruebas de integración: Producto - Inventario (Alertas de Stock)

1. Introducción.
    Propósito: Verificar que el módulo de Inventario gestiona correctamente las alertas de stock relacionadas con los productos y que estas se actualizan conforme a las modificaciones realizadas.

2. Alcance.
    Incluido:
    - Módulo de Producto
    - Módulo de Inventario

3. Criterios de aceptación:
    - Las alertas de stock deben generarse automáticamente cuando el inventario de un producto alcanza un valor mínimo predefinido.
    - El administrador debe poder actualizar el stock y verificar que las alertas se eliminan si el nivel de inventario es adecuado.
    - La eliminación o adición de productos debe reflejarse en el inventario sin errores.

4. Casos de prueba.

    - ID de prueba: PI-001
        - Descripción: Probar la actualización del stock en el inventario y su relación con las alertas de productos.
        - Precondiciones: Los módulos de Producto e Inventario deben estar implementados y compilados correctamente.
        - Componentes involucrados:
            - Módulo de Producto
            - Módulo de Inventario
        - Pasos a seguir:
            1. Iniciar el módulo de Inventario.
            2. Agregar varios productos al inventario con diferentes niveles de stock.
            3. Configurar el nivel de alerta mínima de stock para cada producto.
            4. Reducir el nivel de stock de un producto por debajo del umbral.
            5. Verificar que se genera una alerta de stock bajo.
            6. Actualizar el stock del producto a un nivel aceptable.
            7. Verificar que la alerta desaparece.
        - Resultado esperado:
            - Las alertas de stock bajo se generan y eliminan correctamente según las condiciones establecidas.
        - Resultado real: Las alertas se generaron y eliminaron según lo esperado.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-002
        - Descripción: Verificar que la eliminación de productos afecta el inventario sin errores.
        - Precondiciones: Módulos funcionales.
        - Componentes involucrados:
            - Módulo de Producto
            - Módulo de Inventario
        - Pasos a seguir:
            1. Iniciar el módulo de Inventario.
            2. Agregar un producto al inventario.
            3. Eliminar el producto del inventario.
            4. Verificar que el producto ya no existe en la lista de inventario.
        - Resultado esperado:
            - El producto se elimina del inventario sin generar errores en las conexiones o en los registros relacionados.
        - Resultado real: El producto se eliminó correctamente del inventario.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-003
        - Descripción: Probar la actualización de la información de un producto en el inventario.
        - Precondiciones: Productos previamente agregados al inventario.
        - Componentes involucrados:
            - Módulo de Producto
            - Módulo de Inventario
        - Pasos a seguir:
            1. Iniciar el módulo de Inventario.
            2. Seleccionar un producto existente en el inventario.
            3. Modificar la información del producto, como precio o descripción.
            4. Guardar los cambios y verificar que se reflejen correctamente en el inventario.
        - Resultado esperado:
            - Los cambios realizados en el producto se reflejan en el inventario sin inconsistencias.
        - Resultado real: La información del producto se actualizó correctamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-004
        - Descripción: Verificar que al agregar productos nuevos se actualiza la lista de inventario correctamente.
        - Precondiciones: El módulo de Inventario debe estar inicializado.
        - Componentes involucrados:
            - Módulo de Producto
            - Módulo de Inventario
        - Pasos a seguir:
            1. Iniciar el módulo de Inventario.
            2. Agregar un nuevo producto con atributos válidos.
            3. Verificar que el producto aparece en la lista de inventario.
        - Resultado esperado:
            - El nuevo producto aparece correctamente en el inventario.
        - Resultado real: El producto fue añadido y aparece correctamente.
        - Observaciones: N/A
        - Aprobación: Aprobada

    - ID de prueba: PI-005
        - Descripción: Verificar que el sistema no permite añadir productos duplicados.
        - Precondiciones: Un producto con los mismos atributos ya existe en el inventario.
        - Componentes involucrados:
            - Módulo de Producto
            - Módulo de Inventario
        - Pasos a seguir:
            1. Iniciar el módulo de Inventario.
            2. Intentar agregar un producto que ya existe en el inventario.
            3. Verificar que el sistema rechaza la operación y genera un mensaje de error.
        - Resultado esperado:
            - El sistema no permite productos duplicados y muestra un mensaje de error adecuado.
        - Resultado real: El sistema rechazó el producto duplicado con un mensaje de error claro.
        - Observaciones: N/A
        - Aprobación: Aprobada
"""
