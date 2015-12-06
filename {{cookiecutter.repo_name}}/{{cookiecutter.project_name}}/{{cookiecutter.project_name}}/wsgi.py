"""
WSGI config for xd project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_MODE', 'Production')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "xd.settings")

application = get_wsgi_application()
