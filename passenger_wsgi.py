import os
import sys

import django.core.handlers.wsgi
from django.core.wsgi import get_wsgi_application

# # Set up paths and environment variables
# sys.path.append(os.getcwd())
# os.environ['DJANGO_SETTINGS_MODULE'] = 'nahor.settings'

# # Set script name for the PATH_INFO fix below
# SCRIPT_NAME = os.getcwd()

# class PassengerPathInfoFix(object):
#     """
#         Sets PATH_INFO from REQUEST_URI because Passenger doesn't provide it.
#     """
#     def __init__(self, app):
#         self.app = app

#     def __call__(self, environ, start_response):
#         from urllib.parse import unquote
#         environ['SCRIPT_NAME'] = SCRIPT_NAME
#         request_uri = unquote(environ['REQUEST_URI'])
#         script_name = unquote(environ.get('SCRIPT_NAME', ''))
#         offset = request_uri.startswith(script_name) and len(environ['SCRIPT_NAME']) or 0
#         environ['PATH_INFO'] = request_uri[offset:].split('?', 1)[0]
#         return self.app(environ, start_response)

# # Set the application
application = get_wsgi_application()
# application = PassengerPathInfoFix(application)
