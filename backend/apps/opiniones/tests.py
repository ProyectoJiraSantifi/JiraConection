"""
Prueba de unidad: Módulo Opiniones y Calificaciones.
1. Introducción.
Propósito:
Validar que el módulo de opiniones y calificaciones funcione correctamente, garantizando que los usuarios puedan registrar, ver y filtrar opiniones de productos.

2. Alcance.
Incluido:

	* Registro de opiniones y calificaciones.
	* Visualización de opiniones por producto.
	* Filtrado de opiniones.
3. Criterios de aceptación:

	1.-Los usuarios registrados pueden dejar opiniones únicamente para productos 	comprados.
	2.-La calificación promedio de un producto se calcula correctamente.
	3.-Los filtros funcionan de acuerdo con las opciones seleccionadas.
	4.-Solo los usuarios autenticados pueden modificar o eliminar sus propias 	opiniones.

------------------------------------------------------------------------------------------------------------

4. Casos de prueba.
- ID de prueba: OP-001

- Descripción: Verificar que un usuario registrado pueda dejar una opinión válida.

- Precondiciones:

	1.-El usuario debe estar autenticado.
	2.-El usuario debe haber comprado el producto.

Pasos a seguir:

	1.-Iniciar sesión en la plataforma.
	2.-Acceder a un producto previamente comprado.
	3.-Redactar un comentario y asignar una calificación entre 1 y 5 estrellas.
	4.-Hacer clic en “Enviar opinión”.
Resultado esperado:
La opinión se guarda correctamente y aparece en la sección de opiniones del producto.

Resultado real:
<Resultado de la operación>

Observaciones:
N/A

Aprobación: Negada - Aprobada
---------------------------------------------------------------------

- ID de prueba: OP-002

- Descripción: Verificar que el promedio de calificaciones de un producto se calcule correctamente.

- Precondiciones:

	1.-El producto debe tener al menos dos opiniones registradas.
Pasos a seguir:

	2.-Revisar las calificaciones de un producto con múltiples opiniones.
	3.-Comparar el promedio mostrado con la fórmula estándar de cálculo del promedio.
Resultado esperado:
El promedio de calificaciones se calcula correctamente y refleja los datos reales.

Resultado real:
<Resultado de la operación>

Observaciones:
N/A

Aprobación: Negada - Aprobada
-----------------------------------------------------------

- ID de prueba: OP-003

- Descripción: Verificar que los filtros de calificación funcionen correctamente.

- Precondiciones:

El producto debe tener opiniones con distintas calificaciones.
Pasos a seguir:

	1.-Acceder a un producto con múltiples opiniones.
	2.-Aplicar un filtro para mostrar solo las opiniones de 5 estrellas.
	3.-Aplicar un filtro para mostrar opiniones más recientes.
Resultado esperado:
El sistema muestra únicamente las opiniones que cumplen con los criterios de filtrado seleccionados.

Resultado real:
<Resultado de la operación>

Observaciones:
N/A

Aprobación: Negada - Aprobada
----------------------------------------------------------------------
- ID de prueba: OP-004

- Descripción: Verificar que un usuario pueda editar su propia opinión.

- Precondiciones:

El usuario debe estar autenticado.
El usuario debe haber registrado previamente una opinión para el producto en cuestión.
Pasos a seguir:

	1.-Iniciar sesión en la plataforma.
	2.-Acceder al producto donde el usuario ya dejó una opinión.
	3.-Hacer clic en el botón “Editar opinión”.
	4.-Modificar el comentario y/o la calificación.
	5.-Hacer clic en “Guardar cambios”.
Resultado esperado:
La opinión actualizada se guarda correctamente y muestra las modificaciones realizadas.

Resultado real:
<Resultado de la operación>

Observaciones:
N/A

Aprobación: Negada - Aprobada




"""