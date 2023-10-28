#!/usr/bin/python3
""" a script to route json data """
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.review import Review


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ a route to the statue"""
    return jsonify({'status': 'OK'})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """a function that return all storage json"""
    return {"amenities": storage.count(Amenity), "cities": storage.count(City),
            "places": storage.count(Place),"reviews": storage.count(Review),
            "states": storage.count(State), "users": storage.count(User)}
