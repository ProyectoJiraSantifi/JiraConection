"""
Este módulo configura la aplicación ASGI para el proyecto Django.

ASGI (Asynchronous Server Gateway Interface) es una especificación que permite manejar solicitudes asíncronas en aplicaciones web de Python. Este archivo es necesario para desplegar el proyecto Django en servidores que soportan ASGI, permitiendo así el manejo de conexiones WebSocket y otras funcionalidades asíncronas.

El archivo `asgi.py` expone una instancia de la aplicación ASGI del proyecto Django, que puede ser utilizada por servidores compatibles con ASGI para servir la aplicación.

Atributos:
    application (ASGIHandler): La instancia de la aplicación ASGI del proyecto Django.
"""
