"""
Prueba de integración: Componente Carrito - Inventario.

    1. Introducción.
        Propósito: Validar la integración entre el Componente de Carrito y el Componente de Inventario, asegurando que las 
        operaciones de agregar, modificar y eliminar productos en el carrito se reflejen correctamente en el inventario de 
        productos, actualizando las cantidades y gestionando el stock disponible.

    2. Alcance.
        Incluido: Componente Carrito y Componente Inventario

    3. Criterios de aceptación:
        - El sistema debe reducir la cantidad de un producto en el inventario al agregarlo al carrito.
        - El sistema debe devolver la cantidad de un producto al inventario si se elimina del carrito.
        - El sistema debe verificar el stock disponible antes de permitir que el usuario agregue productos al carrito.
        - El sistema debe actualizar el inventario correctamente cuando el usuario modifique la cantidad de productos en el carrito.

    4. Casos de prueba.

        - ID de prueba: PI-001

        - Descripción: Verificar que la cantidad en el inventario se reduzca al agregar un producto al carrito.

        - Precondiciones: El usuario accede a la vista del producto y el inventario tiene suficiente stock.

        - Componentes involucrados:
            - Componente Carrito y Componente Inventario

        Pasos a seguir:
            1. Seleccionar un producto en el carrito con cantidad inicial en inventario de 20 unidades.
            2. Agregar 5 unidades del producto al carrito.
            3. Verificar que la cantidad en inventario se haya reducido a 15 unidades.

        Resultado esperado: La cantidad en inventario se reduce correctamente al agregar el producto al carrito.

        Resultado real: Inventario actualizado a 15 unidades después de agregar al carrito.

        Observaciones: N/A

        Aprobación: Aprobada

        - ID de prueba: PI-002

        - Descripción: Verificar que el inventario se actualice cuando el usuario elimina un producto del carrito.

        - Precondiciones: El usuario tiene 3 unidades de un producto en el carrito, y el inventario inicial es de 10 unidades.

        - Componentes involucrados:
            - Componente Carrito y Componente Inventario

        Pasos a seguir:
            1. Acceder al carrito y eliminar el producto con 3 unidades.
            2. Verificar que el inventario se actualice y refleje un total de 13 unidades.

        Resultado esperado: La cantidad del inventario se actualiza correctamente cuando se elimina el producto del carrito.

        Resultado real: Inventario actualizado a 13 unidades tras eliminación del producto en el carrito.

        Observaciones: La operación de devolución al inventario funciona como se espera.

        Aprobación: Aprobada

        - ID de prueba: PI-003

        - Descripción: Verificar que el sistema impida al usuario agregar una cantidad mayor al stock disponible en el inventario.

        - Precondiciones: El stock disponible en inventario es de 5 unidades.

        - Componentes involucrados:
            - Componente Carrito y Componente Inventario

        Pasos a seguir:
            1. Intentar agregar 10 unidades de un producto con stock de 5 unidades al carrito.
            2. Verificar que el sistema muestre un mensaje de error indicando que la cantidad solicitada excede el stock disponible.

        Resultado esperado: El sistema muestra un mensaje de error y no permite agregar una cantidad mayor al stock disponible.

        Resultado real: Mensaje de error mostrado: "Cantidad solicitada excede el stock disponible."

        Observaciones: La validación del stock en el inventario es efectiva.

        Aprobación: Aprobada

        - ID de prueba: PI-004

        - Descripción: Verificar que la cantidad en el inventario se ajuste al modificar la cantidad de un producto en el carrito.

        - Precondiciones: El usuario tiene 2 unidades de un producto en el carrito y el inventario muestra 8 unidades restantes.

        - Componentes involucrados:
            - Componente Carrito y Componente Inventario

        Pasos a seguir:
            1. Modificar la cantidad en el carrito de 2 unidades a 4 unidades para el producto seleccionado.
            2. Verificar que la cantidad en el inventario disminuya de 8 a 6 unidades.

        Resultado esperado: La cantidad en inventario se ajusta correctamente al modificar la cantidad en el carrito.

        Resultado real: Cantidad en inventario ajustada a 6 unidades tras modificación en el carrito.

        Observaciones: N/A

        Aprobación: Aprobada

        - ID de prueba: PI-005

        - Descripción: Verificar que el inventario restaure la cantidad completa de un producto cuando se cancela una compra desde el carrito.

        - Precondiciones: El usuario tiene 5 unidades de un producto en el carrito y el inventario muestra 15 unidades restantes.

        - Componentes involucrados:
            - Componente Carrito y Componente Inventario

        Pasos a seguir:
            1. Cancelar la compra desde el carrito.
            2. Verificar que el inventario restaure las 5 unidades al stock inicial, sumando a un total de 20 unidades.

        Resultado esperado: La cantidad del inventario se restaura completamente al cancelar la compra.

        Resultado real: Inventario restaurado a 20 unidades tras cancelar la compra.

        Observaciones: N/A

        Aprobación: Aprobada
"""
