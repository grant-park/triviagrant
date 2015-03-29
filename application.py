"""
This script runs the applicationlication using a development server.
It contains the definition of routes and views for the applicationlication.
"""

from flask import Flask
application = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = application.wsgi_app

from routes import *

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    application.run(HOST, PORT)
