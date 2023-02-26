#!/bin/sh

gunicorn -b 0.0.0.0:8080 Backend:"create_app()" -w 4 --threads 4
