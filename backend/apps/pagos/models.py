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
"""
Clase Pago
 
Atributos:
 
	idPago (int): Identificador único del pago.
	metodoDePago (str): Método de pago utilizado, como PayPal o Mercado Libre.
	monto (float): Monto total del pago.
	estado (str): Estado actual del pago (ejemplo: pendiente, completado, fallido).
	idUsuario (Usuario): Referencia al usuario que realiza el pago.
Métodos:
 
procesarPago():
	Realiza el procesamiento del pago digital mediante el método especificado en el atributo metodoDePago.
	Si el método es PayPal, invoca el método procesarPagoConPayPal().
	Si el método es Mercado Libre, invoca el método procesarPagoConMercadoLibre().
 
verificarPago(): Verifica si el pago fue exitoso consultando la respuesta de la plataforma (PayPal o Mercado Libre) y actualiza el estado en consecuencia.
 
procesarPagoConPayPal(): Implementa el procesamiento de pago a través de la API de PayPal, incluyendo:
	Redirección al sitio de PayPal para autenticación.
	Confirmación del pago y actualización del estado según la respuesta.
 
procesarPagoConMercadoLibre(): Implementa el procesamiento de pago a través de la API de Mercado Libre, incluyendo:
	Autenticación mediante token en Mercado Libre.
	Confirmación del pago y actualización del estado según la respuesta de la plataforma.
 
Implementación de Métodos Digitales de Pago:
 
agregarMetodoDePago():
	Método que permite agregar una nueva plataforma de pago digital en el sistema, configurando los datos de autenticación y el proceso específico de cada nueva 	plataforma.
 
procesarPagoPersonalizado(metodo):
	Realiza el procesamiento para una plataforma digital personalizada utilizando una estructura de plugins o configuración específica para nuevos métodos.
Relación con la clase Pedido:
 
Relación uno a uno entre Pedido y Pago: Un pedido puede tener solo un pago asociado, y cada pago corresponde a un único pedido específico.




"""
