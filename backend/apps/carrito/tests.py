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

"""
Prueba de integración: Componente Producto - Carrito.

    1. Introducción.
        Propósito: Validar la integración entre el Componente de Producto y el Componente de Carrito, asegurando que la 
        funcionalidad de agregar productos, ajustar cantidades y eliminar artículos en el carrito funcione correctamente 
        en conjunto con la selección y gestión de productos en el sistema.

    2. Alcance.
        Incluido: Componente Producto y Componente Carrito

    3. Criterios de aceptación:
        - El sistema permite agregar un producto desde el Componente de Producto al Carrito y muestra el artículo en la lista de compras.
        - El sistema permite modificar la cantidad de un producto en el carrito desde la vista de Producto y refleja estos cambios en 
          el Carrito.
        - El sistema elimina el producto del Carrito si el usuario selecciona la cantidad 0 desde el Componente Producto.
        - El sistema maneja adecuadamente errores si el usuario intenta agregar una cantidad mayor al stock disponible.

    4. Casos de prueba.

        - ID de prueba: PI-001

        - Descripción: Verificar que se puede agregar un producto al carrito desde la vista de Producto.

        - Precondiciones: El usuario accede a la vista de Producto y el producto seleccionado tiene stock disponible.

        - Componentes involucrados:
            - Componente Producto y Componente Carrito

        Pasos a seguir:
            1. Iniciar el Componente Producto y seleccionar un producto.
            2. Ingresar una cantidad válida y hacer clic en "Agregar al carrito".
            3. Acceder al Componente Carrito y verificar que el producto se muestra con la cantidad especificada.

        Resultado esperado: El producto aparece en el carrito con la cantidad seleccionada.

        Resultado real: Producto agregado al carrito con la cantidad seleccionada.

        Observaciones: N/A

        Aprobación: Aprobada

        - ID de prueba: PI-002

        - Descripción: Verificar que el sistema permita ajustar la cantidad de un producto en el carrito desde la vista de Producto.

        - Precondiciones: El usuario tiene un producto en el carrito y desea ajustar la cantidad.

        - Componentes involucrados:
            - Componente Producto y Componente Carrito

        Pasos a seguir:
            1. Acceder al Componente Producto y seleccionar el producto que está en el carrito.
            2. Modificar la cantidad y hacer clic en "Actualizar cantidad en carrito".
            3. Acceder al Componente Carrito y verificar que la cantidad actualizada esté reflejada correctamente.

        Resultado esperado: La cantidad en el carrito se ajusta a la nueva cantidad seleccionada en el Componente Producto.

        Resultado real: Cantidad actualizada correctamente en el carrito.

        Observaciones: La actualización de cantidad es reflejada sin problemas.

        Aprobación: Aprobada

        - ID de prueba: PI-003

        - Descripción: Verificar que el sistema elimine el producto del carrito si el usuario selecciona la cantidad 0 desde la vista de 
         Producto.

        - Precondiciones: El usuario tiene un producto en el carrito.

        - Componentes involucrados:
            - Componente Producto y Componente Carrito

        Pasos a seguir:
            1. Acceder al Componente Producto y seleccionar el producto en el carrito.
            2. Cambiar la cantidad a 0 y hacer clic en "Actualizar cantidad en carrito".
            3. Verificar que el producto ya no esté en la lista de artículos en el carrito.

        Resultado esperado: El producto se elimina automáticamente del carrito al cambiar la cantidad a 0.

        Resultado real: Producto eliminado del carrito al establecer cantidad a 0.

        Observaciones: N/A

        Aprobación: Aprobada

        - ID de prueba: PI-004

        - Descripción: Verificar que el sistema no permita agregar una cantidad mayor al stock disponible en el Componente Producto.

        - Precondiciones: El producto seleccionado tiene un stock limitado.

        - Componentes involucrados:
            - Componente Producto y Componente Carrito

        Pasos a seguir:
            1. Acceder al Componente Producto y seleccionar un producto con stock de 5 unidades.
            2. Intentar agregar una cantidad mayor (por ejemplo, 10 unidades) al carrito.
            3. Verificar que el sistema muestra un mensaje de error.

        Resultado esperado: El sistema muestra un mensaje de error indicando que la cantidad excede el stock disponible.

        Resultado real: Mensaje de error mostrado: "Cantidad solicitada excede el stock disponible."

        Observaciones: La validación de stock en el Componente Producto es efectiva.

        Aprobación: Aprobada

        - ID de prueba: PI-005

        - Descripción: Verificar que el total del carrito se actualice correctamente al agregar múltiples productos desde el Componente Producto.

        - Precondiciones: El usuario selecciona y agrega varios productos con diferentes cantidades y precios desde el Componente Producto.

        - Componentes involucrados:
            - Componente Producto y Componente Carrito

        Pasos a seguir:
            1. Acceder al Componente Producto y agregar varios productos al carrito.
            2. Acceder al Componente Carrito y verificar que el total refleja correctamente las cantidades y precios de los productos agregados.

        Resultado esperado: El total del carrito se actualiza correctamente con todos los productos y cantidades.

        Resultado real: Total del carrito calculado y mostrado correctamente.

        Observaciones: La suma de precios es exacta.

        Aprobación: Aprobada
"""

"""
Prueba de unidad: Módulo "Agregar productos al carrito".

    1. Introducción.
        Propósito: El propósito de estas pruebas es validar que el módulo de agregar productos al carrito funcione 
        correctamente, permitiendo al usuario seleccionar productos, ajustar cantidades y agregar productos al carrito de compras.

    2. Alcance.
        Incluido: Selección de productos, ajuste de cantidad, agregación al carrito, validación de 
        stock y notificación de error si es necesario.

    3. Criterios de aceptación:
        - El usuario debe poder seleccionar un producto y ver su información.
        - El sistema debe permitir al usuario seleccionar una cantidad válida del producto.
        - El producto debe ser agregado al carrito correctamente con la cantidad seleccionada.
        - El sistema debe validar que la cantidad no exceda el stock disponible.
        - El sistema debe mostrar una confirmación de que el producto fue agregado al carrito correctamente.

    4. Casos de prueba.

        - ID de prueba: U-001
        - Descripción: Verificar que un producto puede ser agregado al carrito con la cantidad seleccionada.
        - Precondiciones: El usuario ha accedido correctamente a la vista del producto.
        
        Pasos a seguir:
            1. Seleccionar un producto de la vista de productos.
            2. Ajustar la cantidad del producto a agregar al carrito.
            3. Hacer clic en el botón "Agregar al carrito".
        
        Resultado esperado: El producto con la cantidad seleccionada es agregado al carrito correctamente.
        
        Resultado real: Producto con la cantidad seleccionada agregado exitosamente al carrito.
        
        Observaciones: N/A
        
        Aprobación: Aprobada
        
        - ID de prueba: U-002
        - Descripción: Verificar que el sistema no permita agregar una cantidad mayor al stock disponible.
        - Precondiciones: El usuario ha accedido correctamente a la vista del producto y el stock disponible es 10 unidades.
        
        Pasos a seguir:
            1. Seleccionar un producto con un stock de 10 unidades.
            2. Ajustar la cantidad a 12 unidades.
            3. Hacer clic en el botón "Agregar al carrito".
        
        Resultado esperado: El sistema debe mostrar un mensaje de error indicando que la cantidad excede el stock disponible.
        
        Resultado real: Error mostrado correctamente: "La cantidad seleccionada excede el stock disponible."
        
        Observaciones: El sistema bloquea la cantidad no válida correctamente.
        
        Aprobación: Aprobada
        
        - ID de prueba: U-003
        - Descripción: Verificar que el sistema no permita agregar una cantidad no válida (por ejemplo, 0 unidades).
        - Precondiciones: El usuario ha accedido correctamente a la vista del producto.
        
        Pasos a seguir:
            1. Seleccionar un producto.
            2. Ajustar la cantidad a 0.
            3. Hacer clic en el botón "Agregar al carrito".
        
        Resultado esperado: El sistema debe mostrar un mensaje de error indicando que la cantidad debe ser mayor que 0.
        
        Resultado real: Mensaje de error mostrado: "La cantidad debe ser mayor a 0."
        
        Observaciones: El sistema permite ingresar solo valores positivos, lo cual es correcto.
        
        Aprobación: Aprobada
        
        - ID de prueba: U-004
        - Descripción: Verificar que el sistema confirme que el producto fue agregado al carrito.
        - Precondiciones: El usuario ha accedido correctamente a la vista del producto.
        
        Pasos a seguir:
            1. Seleccionar un producto.
            2. Ajustar la cantidad a 1 unidad.
            3. Hacer clic en el botón "Agregar al carrito".
        
        Resultado esperado: El sistema debe mostrar un mensaje confirmando que el producto fue agregado al carrito.
        
        Resultado real: Mensaje de confirmación mostrado: "Producto agregado al carrito correctamente."
        
        Observaciones: N/A
        
        Aprobación: Aprobada
        
        - ID de prueba: U-005
        - Descripción: Verificar que el usuario puede agregar múltiples productos al carrito.
        - Precondiciones: El usuario ha accedido correctamente a la vista de productos.
        
        Pasos a seguir:
            1. Seleccionar un producto y agregarlo al carrito.
            2. Regresar a la vista de productos y seleccionar un segundo producto.
            3. Ajustar la cantidad del segundo producto.
            4. Hacer clic en "Agregar al carrito".
        
        Resultado esperado: Ambos productos son agregados al carrito correctamente.
        
        Resultado real: Múltiples productos agregados al carrito exitosamente.
        
        Observaciones: La navegación entre productos y la actualización del carrito funcionan correctamente.
        
        Aprobación: Aprobada
"""
