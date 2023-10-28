#!/usr/bin/python3
""" main flask app route"""
from os import getenv
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down(self):
    storage.close()


@app.errorhandler(404)
def not_found(e):
    """ 404 error handler"""
    return jsonify({"error": "Not found"})


if __name__ == "__main__":
    """ getenv for main app"""
    host = getenv('HBNB_API_HOST')
    port = getenv('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
