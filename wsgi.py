import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'appsembler_settings'

import django.core.handlers.wsgi as w
application = w.WSGIHandler()
