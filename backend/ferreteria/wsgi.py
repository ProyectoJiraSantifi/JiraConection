"""
El archivo wsgi.py en un proyecto Django sirve como punto de entrada para los servidores web compatibles con WSGI (Web Server Gateway Interface) para servir la aplicación web Django. WSGI es una especificación que describe cómo un servidor web se comunica con aplicaciones web en Python. Este archivo configura el entorno de la aplicación y expone una variable llamada `application` que el servidor web utiliza para interactuar con la aplicación Django.

Funciones principales del archivo wsgi.py:
- Configurar el entorno de Django.
- Exponer la aplicación WSGI para que el servidor web pueda manejar las solicitudes HTTP.

Este archivo es esencial para desplegar la aplicación Django en un entorno de producción.
"""
