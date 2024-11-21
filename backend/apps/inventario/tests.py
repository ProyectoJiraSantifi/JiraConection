"""
Prueba de rendimiento: Gestión de productos en inventario  

1. Introducción
Propósito: 
    Validar el tiempo de respuesta y la estabilidad del sistema al agregar y 
    eliminar productos del inventario bajo diferentes cargas de usuarios en el sistema.  

2. Alcance  
Incluido:  
- Rendimiento al agregar y eliminar productos en el inventario.  

3. Criterios de aceptación  
- Operaciones realizadas en menos de 2 segundos con hasta 1000 usuarios simultáneos.  
- Cambios reflejados correctamente en el sistema sin fallos.  

4. Casos de prueba  

ID de prueba: PR-001  

Descripción: 
    Validar el tiempo de respuesta al agregar productos al inventario.  
Precondiciones:  
  1. Base de datos con 10,000 productos existentes.  
  2. Acceso activo al módulo de inventario.  

Cargas de prueba:  
- Simulación de 1000 usuarios simultáneos agregando productos al inventario.  

Pasos a seguir:  
1. Iniciar sesión como administrador.  
2. Navegar al módulo "Gestión de inventario".  
3. Agregar un nuevo producto con los siguientes datos:  
   - Nombre: "Producto de prueba".  
   - Stock inicial: 50 unidades.  
   - Precio: $25.00.  
4. Medir el tiempo de respuesta del sistema.  

Resultado esperado:  
- Tiempo de respuesta: ≤ 2 segundos.  
- Producto agregado correctamente.  

Resultado real:  
- Tiempo promedio de respuesta: **1.8 segundos**.  
- Producto agregado exitosamente sin errores.  

Observaciones:  
    El sistema manejó la carga de usuarios simultáneos de manera eficiente.  

Aprobación:  
    Aprobada  

---

ID de prueba: PR-002
  
Descripción: 
    Validar el tiempo de respuesta al eliminar productos del inventario.  
Precondiciones:  
  1. Base de datos con 10,000 productos existentes.  
  2. Acceso activo al módulo de inventario.  

Cargas de prueba:  
- Simulación de 1000 usuarios simultáneos eliminando productos del inventario.  

Pasos a seguir:  
1. Iniciar sesión como administrador.  
2. Navegar al módulo "Gestión de inventario".  
3. Seleccionar un producto existente y eliminarlo.  
4. Medir el tiempo de respuesta del sistema.  

Resultado esperado:  
- Tiempo de respuesta: ≤ 2 segundos.  
- Producto eliminado correctamente.  

Resultado real:  
- Tiempo promedio de respuesta: **2.1 segundos**.  
- Producto eliminado exitosamente.  

Observaciones:  
El tiempo de respuesta excedió levemente el límite establecido bajo alta carga, pero la operación fue funcional.  

Aprobación:  
    Negada (con observación).  

-------------------------------

Prueba de interfaz de usuario: Gestión de productos en inventario  

1. Introducción  
Propósito: 
    Asegurar que la interfaz permita agregar y eliminar productos del inventario de manera intuitiva, 
    mostrando los resultados de manera inmediata.  

2. Alcance  
Incluido:  
- Operaciones realizadas desde la interfaz: agregar y eliminar productos.  

3. Criterios de aceptación  
- La interfaz debe reflejar los cambios inmediatamente.  
- Mensajes de confirmación claros al completar las acciones.  

4. Casos de prueba  

ID de prueba: IUI-001

Descripción: Verificar la funcionalidad para agregar productos desde la interfaz de usuario.  
Precondiciones:  
  1. Acceso al módulo de gestión de inventario como administrador.  

Pasos a seguir:  
1. Iniciar sesión en el panel de administración.  
2. Navegar al módulo "Gestión de inventario".  
3. Hacer clic en "Agregar producto".  
4. Ingresar los datos:  
   - Nombre: "Producto Demo".  
   - Stock inicial: 100 unidades.  
   - Precio: $50.00.  
5. Hacer clic en "Guardar".  

Resultado esperado:  
- El producto aparece inmediatamente en la lista de inventario.  
- Se muestra un mensaje de confirmación: _"Producto agregado exitosamente."_  

Resultado real:  
- El producto "Producto Demo" fue agregado correctamente.  
- Tiempo para reflejar el cambio: **1.5 segundos**.  
- Mensaje mostrado: _"Producto agregado exitosamente."_  

Observaciones:  
    La operación fue rápida y la interfaz es clara e intuitiva.  

Aprobación:  
    Aprobada 

-------------------------------

ID de prueba: IUI-002  

Descripción: 
    Verificar la funcionalidad para eliminar productos desde la interfaz de usuario.  
Precondiciones:  
  1. Existe un producto llamado "Producto Demo" en el inventario.  

Pasos a seguir:  
1. Iniciar sesión en el panel de administración.  
2. Navegar al módulo "Gestión de inventario".  
3. Seleccionar el producto "Producto Demo".  
4. Hacer clic en "Eliminar".  
5. Confirmar la acción en el cuadro emergente.  

Resultado esperado:  
- El producto desaparece de la lista de inventario inmediatamente.  
- Se muestra un mensaje de confirmación: _"Producto eliminado exitosamente."_  

Resultado real:  
- El producto "Producto Demo" fue eliminado correctamente.  
- Tiempo para reflejar el cambio: **1.8 segundos**.  
- Mensaje mostrado: _"Producto eliminado exitosamente."_  

Observaciones:  
    La eliminación fue precisa, con retroalimentación clara para el usuario.  

Aprobación:  
    Aprobada  

-------------------------------

Resumen:  
    Las pruebas mostraron un rendimiento sólido en operaciones regulares, aunque 
    se observó un leve retraso bajo alta carga en la eliminación de productos. 
    La interfaz fue funcional e intuitiva, ofreciendo una experiencia fluida para los administradores.  
"""