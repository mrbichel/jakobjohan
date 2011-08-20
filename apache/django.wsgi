import os
import sys
import site

site.addsitedir('/home/johan/.virtualenvs/jakobjohan/lib/python2.7/site-packages')

sys.path.append('/home/johan/srv/')
sys.path.append('/home/johan/srv/jakobjohan/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'jakobjohan.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()