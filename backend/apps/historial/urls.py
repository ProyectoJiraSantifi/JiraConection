'''
    url('historial/<id_pedido>/', ver_historial, name='ver_historial'),  # Visualizar un pedido específico en el historial
    url('historial/filtro/', filtrar_historial, name='filtrar_historial'),  # Filtrar historial de compras por diferentes criterios
    url('historial/', historial_compras, name='historial_compras'),  # Ver todo el historial de compras
    url('pedidos/filtro/', filtrar_pedidos, name='filtrar_pedidos'),  # Filtrar pedidos según diferentes criterios
    url('pedidos/<id_pedido>/', ver_pedido, name='ver_pedido'),  # Ver detalles de un pedido específico
    url('pedidos/', lista_pedidos, name='lista_pedidos'),  # Ver todos los pedidos
'''