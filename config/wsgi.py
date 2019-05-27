import os
from django.core.wsgi import get_wsgi_application


SETTINGS_MODULE = os.environ.get('SETTINGS', 'config.settings.local')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)
application = get_wsgi_application()
