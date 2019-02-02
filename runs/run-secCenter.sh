#!/bin/bash

/usr/local/bin/uwsgi --http :87 --chdir /opt/secCenter --wsgi-file /opt/secCenter/secCenter/wsgi.py --static-map=/static=static
