import os
import sys

path = '/var/apps/zoe/current'
if path not in sys.path:
    sys.path.append(path)

path = '/var/apps/zoe/current/zoe'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'zoe.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

