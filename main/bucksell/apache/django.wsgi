import os
import sys

from os.path import abspath, dirname, join
from site import addsitedir
import sys
# adding external lib folder to the path.
path = '/home/ubuntu/bucksell/code/main/bucksell/'
#path = addsitedir(abspath(join(dirname(__file__), '../libs')), set())
#if path: sys.path = list(path) + sys.path

# updating python sys path to include project applications.

sys.path.insert(0, abspath(join(dirname(__file__), 'apps')))
sys.path.insert(0, abspath(join(dirname(__file__), 'external_apps')))
sys.path.insert(0, abspath(join(dirname(__file__), '../libs')))

if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = '../settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()