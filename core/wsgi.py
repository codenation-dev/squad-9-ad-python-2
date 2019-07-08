"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

value = os.environ["DJANGO_SETTINGS_MODULE"]

if value == "settings.production":
    print("AMBIENTE DE PRODUCAO")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.production')
else:
    print("AMBIENTE DE DESENVOLVIMENTO")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.development')

application = get_wsgi_application()
