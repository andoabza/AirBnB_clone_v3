#!/usr/bin/python3
""" a script to route json data """
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    """ a route to the statue"""
    return jsonify({'status': 'OK'})
