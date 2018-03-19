"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings.dev")

application = get_wsgi_application()

# setting up for django to link with whitenoise on heroku


from whitenoise.django import DjangoWhiteNoise

application = DjangoWhiteNoise(application)
