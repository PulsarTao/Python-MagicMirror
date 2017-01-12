#!usr/bin/python
# -*- coding: utf-8 -*-
"""
This script runs the MagicMirror application using a development server.
"""

from os import environ
from MagicMirror import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    try:
        app.run(host="localhost", port="5555")
    except:
        print Exception