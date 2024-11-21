""" 
Prueba de interfaz de usuario: Alertas por inventario bajo en e-commerce

1. Introducción
Propósito: 
    Validar el correcto funcionamiento de las alertas de inventario bajo en la plataforma, 
    asegurando que los administradores sean notificados cuando el stock de un producto está por debajo del nivel mínimo configurado.  

2. Alcance  
Incluido:  
- Configuración del umbral de inventario mínimo.  
- Visualización y precisión de las alertas en el panel de administración.  

3. Criterios de aceptación  
- El sistema debe generar una alerta automática cuando el stock de un producto está por debajo del nivel mínimo configurado.  
- La alerta debe incluir el nombre del producto, la cantidad actual, y el umbral mínimo configurado.  
- No deben generarse alertas falsas para productos que cumplan con el nivel mínimo o superior.  

4. Casos de prueba

ID de prueba: AUI-001

Descripción: 
    Verificar que se genere una alerta cuando el inventario esté por debajo del nivel mínimo.  
Precondiciones:  
  1. El umbral de inventario mínimo está configurado en 10 unidades para todos los productos.  
  2. El producto "Camiseta Negra" tiene 5 unidades en stock.  

Pasos a seguir:  
1. Iniciar sesión en el panel de administración de "ShopEasy".  
2. Navegar a la sección "Gestión de inventario".  
3. Revisar las alertas generadas automáticamente.  

Resultado esperado:  
- Se genera una alerta con el mensaje:  
  _"Alerta: El producto 'Camiseta Negra' tiene un inventario bajo (5 unidades). Umbral mínimo: 10 unidades."_  

Resultado real:  
- Se generó la alerta esperada:  
  _"Alerta: El producto 'Camiseta Negra' tiene un inventario bajo (5 unidades). Umbral mínimo: 10 unidades."_  

Observaciones:  
    El sistema detectó correctamente el inventario bajo y generó la alerta adecuada.  

Aprobación:  
    Aprobada  

---------------------------------

ID de prueba: AUI-002  

Descripción: 
    Verificar que no se genere una alerta si el inventario está en el nivel mínimo o superior.  
Precondiciones:  
  1. El umbral de inventario mínimo está configurado en 10 unidades.  
  2. El producto "Zapatos Deportivos" tiene 12 unidades en stock.  

Pasos a seguir:  
1. Iniciar sesión en el panel de administración de "ShopEasy".  
2. Navegar a la sección "Gestión de inventario".  
3. Revisar las alertas generadas automáticamente.  

Resultado esperado:  
- No se genera ninguna alerta para el producto "Zapatos Deportivos".  

Resultado real:  
- Ninguna alerta fue generada para "Zapatos Deportivos".  

Observaciones:  
    El sistema no generó alertas erróneas para productos con inventario suficiente.  

Aprobación:  
    Aprobada  

---------------------------------

ID de prueba: AUI-003
  
Descripción: 
    Verificar la actualización de alertas al ajustar el inventario.  
Precondiciones:  
  - Existe una alerta activa para el producto "Camiseta Blanca" (stock: 3 unidades, umbral mínimo: 10 unidades).  

Pasos a seguir:  
1. Actualizar el inventario del producto "Camiseta Blanca" a 15 unidades.  
2. Navegar nuevamente a la sección "Gestión de inventario".  

Resultado esperado:  
- La alerta del producto "Camiseta Blanca" desaparece automáticamente.  

Resultado real:  
- La alerta fue removida correctamente después de la actualización del inventario.  

Observaciones:  
    El sistema respondió de manera adecuada al cambio de stock.  

Aprobación:  
    Aprobada  

---------------------------------

Resumen: 
    Las pruebas demostraron que el sistema de alertas de inventario bajo es preciso, 
    confiable y fácil de gestionar, asegurando que los administradores sean notificados correctamente y puedan tomar decisiones rápidas.

"""
