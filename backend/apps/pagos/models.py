"""
Modelo de Pago
 
Atributos
	-idPago: entero
	-metododePago: string 
	-monto: float
	-estado: string
	-IDUSUARIO: usuario
 
Metodos
	+ProcesarPago(): Realiza el procesamiento del pago utilizando el método de pago especificado.
	+verificarPago(): Verifica si el pago se realizó exitosamente y actualiza el estado en consecuencia.
 
Conexiones:
Pedido:
	Relación uno a uno entre Pedido y Pago: Un pedido puede tener solo un pago asociado, y cada pago corresponde a un único pedido específico.


"""

"""
Modelo de Pago
 
Atributos
	-idPago: entero
	-metododePago: string 
	-monto: float
	-estado: string
	-IDUSUARIO: usuario
 
Metodos
	procesarPago():
	Realiza el procesamiento del pago mediante la plataforma seleccionada (PayPal o Mercado Libre).	
	En el caso de PayPal, incluye la autenticación y redirección a la plataforma de PayPal.
	En el caso de Mercado Libre, se conecta al API correspondiente para procesar el pago.
	verificarPago(): Verifica si el pago fue exitoso consultando la respuesta de la plataforma (PayPal o Mercado Libre) y actualiza el estado en consecuencia.
 
Conexiones:
Pedido:
	Relación uno a uno entre Pedido y Pago: Un pedido puede tener solo un pago asociado, y cada pago corresponde a un único pedido específico.
 
 
Implementación específica para PayPal y Mercado Libre:
procesarPagoConPayPal(): Realiza el procesamiento de pagos a través de PayPal, redirigiendo al usuario y verificando la respuesta de la plataforma.
 
procesarPagoConMercadoLibre(): Procesa el pago mediante el API de Mercado Libre, gestionando los tokens de autenticación y actualizando el estado según la respuesta.





"""