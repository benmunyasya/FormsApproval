import os
import sys
import site
from django.core.wsgi import get_wsgi_application
sys.path.append('C:/Users/bngovi/Desktop/WORKFLOW')
sys.path.append('C:/Users/bngovi/Desktop/WORKFLOW/WORKFLOW')
sys.path.append('C:/Users/bngovi/Desktop/WORKFLOW/access')
os.environ['DJANGO_SETTINGS_MODULE']='WORKFLOW.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WORKFLOW.settings')
application=get_wsgi_application()