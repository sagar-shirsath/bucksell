import os
import sys

from os.path import abspath, dirname, join
from site import addsitedir
import sys
# adding external lib folder to the path.
path = addsitedir(abspath(join(dirname(__file__), '../libs')), set())
if path: sys.path = list(path) + sys.path

# updating python sys path to include project applications.

sys.path.insert(0, abspath(join(dirname(__file__), 'apps')))
sys.path.insert(0, abspath(join(dirname(__file__), 'external_apps')))
sys.path.insert(0, abspath(join(dirname(__file__), '../libs')))
#path = '/home/ubuntu/bucksell/code/main/bucksell/'
if path not in sys.path:
    sys.path.append(path)

try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

os.environ['DJANGO_SETTINGS_MODULE'] = settings

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()