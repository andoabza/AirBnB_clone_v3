#!/usr/bin/python3
""" a script to handle Amenity """
from flask import abort, request, jsonify
from models import storage
from api.v1.views import app_views


@app_views.route('/amenities', strict_slashes=False, methods=['GET'])
def all_amenity():
    """ get all amenities """
    amenity = storage.all('Amenity').values()
    return jsonify(amenity.to_dict())


