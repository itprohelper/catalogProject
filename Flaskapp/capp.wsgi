#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/html/Flaskapp/")

from Flaskapp import app as application
#from application import app as application
application.secret_key = 'Add your secret key'
