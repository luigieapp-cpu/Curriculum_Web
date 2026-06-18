"""ASGI config for curriculum_web project."""
import os

from django.core.asgi import get_asgi_application


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "curriculum_web.settings")

application = get_asgi_application()
