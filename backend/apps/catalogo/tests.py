""" 
Prueba de interfaz de usuario: Filtro de pedidos anteriores  

1. Introducción  
Propósito: 
    Validar la funcionalidad de los filtros en la sección de pedidos, 
    garantizando que los usuarios puedan buscar fácilmente sus compras anteriores por rango de precio o por producto adquirido.  

2. Alcance 
Incluido:  
- Interacción con los filtros "Por precio" y "Por producto".  
- Precisión en la visualización de resultados.  
- Pruebas en la plataforma.  

3. Criterios de aceptación  
- La interfaz debe ser intuitiva, con filtros visibles y fáciles de usar.  
- El sistema debe devolver resultados precisos de acuerdo con los criterios seleccionados.  
- No deben generarse errores al aplicar o borrar los filtros.  

4. Casos de prueba

ID de prueba: PUI-001  
Descripción:
    Verificar el funcionamiento del filtro por rango de precio.  
Precondiciones:  
  1. El usuario tiene 10 pedidos en la plataforma, con precios que varían entre $10 y $200.  
  2. El usuario ha iniciado sesión y accedido a la sección "Mis pedidos".  

Pasos a seguir:  
1. Navegar a la sección "Mis pedidos".  
2. Seleccionar la opción "Filtrar por precio".  
3. Ingresar un rango de precios: $20 a $100.  
4. Hacer clic en "Aplicar filtro".  

Resultado esperado:  
- Se muestran únicamente los pedidos cuyo precio está entre $20 y $100.  
- Los resultados incluyen el número de pedido, el producto, y la fecha de compra.  

Resultado real:  
- Pedidos mostrados:  
  - Pedido #12345: $30  
  - Pedido #12346: $80  

Observaciones:  
    El filtro funcionó correctamente y los resultados coinciden con el rango seleccionado.  

Aprobación:  
    Aprobada  

----------------------------------

ID de prueba: PUI-002
Descripción: 
    Verificar el funcionamiento del filtro por producto comprado.  
Precondiciones:  
  1. El usuario tiene un historial de pedidos con diferentes productos, incluyendo "Camiseta Negra" y "Zapatos Deportivos".  
  2. El usuario ha iniciado sesión y accedido a la sección "Mis pedidos".  

Pasos a seguir:  
1. Navegar a la sección "Mis pedidos".  
2. Seleccionar la opción "Filtrar por producto".  
3. Ingresar el nombre del producto: "Camiseta Negra".  
4. Hacer clic en "Aplicar filtro".  

Resultado esperado:  
- Se muestran únicamente los pedidos que incluyan "Camiseta Negra".  
- Los resultados incluyen el número de pedido, el producto, y la fecha de compra.  

Resultado real:  
- Pedidos mostrados:  
  - Pedido #12347: "Camiseta Negra" - $25  
  - Pedido #12348: "Camiseta Negra" - $27  

Observaciones:  
    El filtro identificó correctamente los pedidos con "Camiseta Negra".  

Aprobación:  
    Aprobada  

----------------------------------

ID de prueba: PUI-003
  
Descripción: 
    Verificar la limpieza de los filtros.  
Precondiciones:  
    El filtro "Por precio" ya ha sido aplicado.  

Pasos a seguir:  
1. Hacer clic en "Limpiar filtros".  
2. Observar la lista de pedidos.  

Resultado esperado:  
- Todos los pedidos del historial del usuario deben volver a ser visibles.  

Resultado real:  
- Se muestran todos los pedidos correctamente.  

Aprobación:  
    Aprobada  
    
----------------------------------

Resumen: 
    Las pruebas realizadas en la plataforma demostraron que los filtros son precisos, 
    rápidos y fáciles de usar, mejorando significativamente la experiencia del usuario al buscar pedidos anteriores.
"""
