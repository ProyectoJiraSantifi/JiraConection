"""
url('pagos/', mostrar_pagos, name='mostrar_pagos'),
url('pagos/procesar/<id_pedido>/', procesar_pago, name='procesar_pago'),
url('pagos/paypal/', procesar_pago_paypal, name='procesar_pago_paypal'),
url('pagos/mercadolibre/', procesar_pago_mercadolibre, name='procesar_pago_mercadolibre'),
url('pagos/confirmar/<id_pago>/', confirmar_pago, name='confirmar_pago'),
url('pagos/cancelar/<id_pago>/', cancelar_pago, name='cancelar_pago'),



"""