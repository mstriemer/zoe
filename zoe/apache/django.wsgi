import os
import sys

# Add the virtual Python environment site-packages directory to the path
import site
site.addsitedir('/var/apps/environments/zoe/lib/python2.7/site-packages')

path = '/var/apps/zoe/current'
if path not in sys.path:
    sys.path.append(path)

path = '/var/apps/zoe/current/zoe'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'zoe.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# Setup Celery
os.environ["CELERY_LOADER"] = "django"
