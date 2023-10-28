#!/usr/bin/python3
""" main flask app route"""
from os import getenv
from flask import Flask
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear(error):
    storage.close()


if __name__ == "__main__":
    """ getenv for main app"""
    HOST = getenv('HBNB_API_HOST')
    PORT = getenv('HBNB_API_PORT')
    if HOST and PORT:
        app.run(host=HOST, port=PORT, threaded=True)
    else:
        app.run(host='0.0.0.0', port='5000', threaded=True)
