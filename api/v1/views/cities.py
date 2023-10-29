#!/usr/bin/python3
"""
module that defines API interactions for State __objects
"""
from models import storage
from models.city import City
from models.state import State
from api.v1.views import app_views
from flask import jsonify, abort, request


@app_views.route('/states/<state_id>/cities', strict_slashes=False,
                 methods=["GET"])
def id_for_city(state_id):
    """
    defines the states/<state_id>/cities route
    Returns: state id or 404 Error if object not linked to State object
    """
    citi = storage.all("City").values()
    a_state = storage.get(State, state_id)
    if a_state:
        return jsonify([cities.to_dict() for cities in citi])
    return abort(404)


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['GET'])
def get_city(city_id):
    """
    defines the cities route
    Returns: list of all State objects
    """
    city = storage.get(City, city_id)
    if city:
        return jsonify(city.to_dict())


@app_views.route('/cities/<cities_id>', strict_slashes=False,
                 methods=['DELETE'])
def delete_city_id(city_id):
    """
    defines DELETE for city objects by id
    Returns: if successful 200 and an empty dictionary
             404 if state_id is not linked to any State obj
    """
    city = storage.get(City, city_id)
    if city:
        storage.delete(city)
        storage.save()
        return jsonify({}), 200
    return abort(404)


@app_views.route('states/<state_id>/cities/', strict_slashes=False,
                 methods=['POST'])
def create_city():
    """
    define how to create a new city objects
    Returns: 201 on successful creation
             400 "Not a JSON" if HTTP body request is not valid
             404 if state_id is not linked to any State object
    """
    a_state = storage.get(State, state_id)
    if a_state:
        try:
            city = request.get_json()

            if city.get("name") is None:
                return abort(400, 'Missing name')
        except Exception:
            return abort(400, 'Not a JSON')

        new_city = City(**city)
        storage.new(new_city)
        storage.save()
        return jsonify(new_city.to_dict()), 201


@app_views.route('/cities/<city_id>', strict_slashes=False, methods=['PUT'])
def city_update(city_id):
    """
    defines how an Update to a city is made
    Returns: 200 and the state object if successful
             400 "Not a JSON" if HTTP body request is not valid
             404 if state_id is not linked to any State object
    """
    city_data = request.get_json()

    if not city_data:
        return abort(400, 'Not a JSON')

    city = storage.get(City, state_id)

    if not city:
        return abort(404)

    for key, value in city_data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    storage.save()

    return jsonify(city.to_dict()), 200
