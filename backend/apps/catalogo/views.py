""" 
Barra de búsqueda: El usuario podrá ingresar un término de búsqueda, y la plataforma
    mostrará productos que coincidan en los campos relevantes, como nombre o descripción.
    Al ingresar una palabra clave, se realizará una consulta a la base de datos, y los 
    resultados se mostrarán inmediatamente en la página.
  
  
Filtros: Los usuarios podrán aplicar varios filtros simultáneamente para limitar
    los resultados según diferentes criterios. Los filtros serán:
    - Categoría: Permite filtrar productos por categorías específicas.
    - Precio: Los usuarios podrán seleccionar un rango de precios.
    - Disponibilidad: Filtra los productos por estado de inventario, como "En stock" o
      "Agotado".
      
      
Resultados: Los productos se actualizarán dinámicamente al aplicar filtros o realizar
    una búsqueda, sin necesidad de recargar la página completa, optimizando la experiencia
    de usuario.
    
    
En esta sección se implementará la funcionalidad para que los usuarios puedan ver
de manera clara y organizada todos los productos disponibles en la ferretería.
La visualización mostrará detalles clave de cada producto, como:
    - Nombre del producto
    - Imagen del producto
    - Descripción breve
    - Precio por unidad
    - Disponibilidad (en stock o agotado)


Componentes incluidos:
Listado de productos: Se mostrará en forma de lista o cuadrícula, donde cada producto
   estará representado por:
   - Imagen del producto: Imagen clara y de alta calidad que facilite la identificación.
   - Nombre del producto: Descripción breve para una identificación rápida.
   - Descripción: Detalles esenciales o especificaciones técnicas relevantes.
   - Precio por unidad: Se mostrará claramente para decisiones de compra informadas.
   - Disponibilidad: Indicador de si el producto está en stock o agotado, con opción de
     notificación para productos agotados.
     
     
Funcionalidad adicional:
    - Paginación: Se implementará para dividir el catálogo en varias páginas, optimizando
    la velocidad y el rendimiento al mostrar un número fijo de productos por página.
    
    
Agregar productos al carrito:
Funcionalidad para que los usuarios puedan agregar productos al carrito de compras de manera 
sencilla y rápida. Al hacer clic en un botón "Agregar al carrito", el producto seleccionado se
agregará al carrito de compras, y se mostrará un mensaje de confirmación. El carrito de compras
mostrará una lista de los productos seleccionados, con la opción de modificar la cantidad o
eliminar productos.
   - Botón "Agregar al carrito": Permite a los usuarios agregar productos al carrito con un clic.
   - Carrito de compras: Muestra una lista de los productos seleccionados, con opciones para
     modificar la cantidad o eliminar productos.
    - Mensaje de confirmación: Se mostrará un mensaje de confirmación al agregar un producto al
        carrito
    - Cantidad: Los usuarios podrán seleccionar la cantidad deseada de cada producto antes de
        agregarlo al carrito.
"""
