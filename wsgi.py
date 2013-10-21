"""
WSGI config
"""
import os, sys


path = '/var/www/arsfest/releases/current/'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tf_arsfest.settings")
os.environ.setdefault("DJANGO_ENVIRONMENT", "hugin")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()