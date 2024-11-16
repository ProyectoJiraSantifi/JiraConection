"""
Visualizacion de productos en el carrito: Cuando el usuario accede a la vista del carrito, el sistema verificara si 
    hay productos agregados. Si hay productos, se mostrara una lista con la siguiente informacion:
       - Nombre del producto.
       - Descripcion breve.
       - Precio unitario.
       - Cantidad seleccionada por el usuario.
       - Total por producto (calculado como Precio unitario x Cantidad).
   - Los datos seran extraidos desde la base de datos y enviados a la plantilla correspondiente.

Calculo del subtotal por producto: Para cada producto, el sistema realizara un calculo dinamico del subtotal 
    (Subtotal = Precio unitario * Cantidad), este subtotal sera mostrado junto con los demas datos del producto.

Calculo del total general del carrito:
   - El sistema sumara los subtotales de todos los productos.
   - Este total general sera enviado a la plantilla para que se muestre en una seccion destacada.

Carrito vacio:
   - Si el usuario no ha agregado productos, el sistema detectara que el carrito esta vacio.
   - Se mostrara un mensaje al usuario indicando: "El carrito esta vacio".
   - No se realizaran calculos y el total a pagar sera igual a $0.

Boton de proceder al pago: Si el carrito contiene productos, el sistema mostrara un boton para continuar 
    al proceso de pago. Al hacer clic en este boton, el usuario sera redirigido a una vista para completar el pago.

"""
