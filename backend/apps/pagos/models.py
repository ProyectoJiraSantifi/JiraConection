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