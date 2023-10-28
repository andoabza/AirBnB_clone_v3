#!/usr/bin/python3
""" a script for the State object"""
from models.base_model import BaseModel
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import jsonify, abort, request


@app_views.route('/states', methods=['GET'], strict_slashes=False)
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def state(state_id=None):
    """show all state or one state if there is state id"""
    if state_id:
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        return jsonify(state.to_dict())
    states = storage.all(State)
    state_list = []
    for state in states.values():
        state_list.append(state.to_dict())
    return jsonify(state_list)


@app_views.route(
        '/states/<state_id>', methods=['DELETE'],
        strict_slashes=False
        )
def delet(state_id):
    """delete state with given state_id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post():
    """ a post for states"""
    data = request.get_json()
    if 'name' in data.keys():
        state = State(**data)
        state.save()
        return jsonify(state.to_dict()), 201
    if not data:
        abort(400, 'Not a JSON')
    abort(400, 'Missing name')


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """put method for the state"""
    data = request.get_json()
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    ignored_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignored_keys:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
    if not data:
        abort(400, 'Not a JSON')
