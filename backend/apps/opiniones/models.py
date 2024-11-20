"""
Modelo de Opiniones y Calificaciones
1. Entidades principales
Usuario

id_usuario (PK): Identificador único del usuario.
nombre: Nombre del usuario.
email: Correo electrónico del usuario.
fecha_registro: Fecha en la que se registró el usuario.
Producto

id_producto (PK): Identificador único del producto.
nombre_producto: Nombre del producto.
descripcion: Descripción del producto.
precio: Precio del producto.
categoria: Categoría del producto (e.g., "Herramientas", "Materiales de construcción").
Opinión

id_opinion (PK): Identificador único de la opinión.
id_usuario (FK): Relación con el usuario que hizo la opinión.
id_producto (FK): Relación con el producto sobre el que se hizo la opinión.
calificacion: Número de estrellas (1-5).
comentario: Texto de la opinión del usuario.
fecha_opinion: Fecha en que se realizó la opinión.

Un usuario puede dejar varias opiniones (1 entre Usuario y Opinión).
Un producto puede tener múltiples opiniones asociadas (1 entre Producto y Opinión).



"""