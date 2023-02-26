import os

from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=True)


    from . import upload

    app.register_blueprint(upload.bp)

    CORS(app)
    return app