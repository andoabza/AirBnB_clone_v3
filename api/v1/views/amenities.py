#!/usr/bin/python3
""" a script to handle Amenity """
from flask import abort, request, jsonify
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity


@app_views.route('/amenities', strict_slashes=False, methods=['GET'])
def all_amenity():
    """ get all amenities """
    amenity = storage.all('Amenity').values()
    return jsonify([a.to_dict() for a in amenity])


@app_views.route('/amenities/<a_id>', strict_slashes=False, methods=['GET'])
def get_amenity(a_id):
    """ gets amenity by it's id"""
    amenity = storage.get(Amenity, a_id)
    if amenity:
        return jsonify(amenity.to_dict())
    abort(404)


@app_views.route('/amenities/<a_id>', strict_slashes=False, methods=['DELETE'])
def del_am(a_id):
    """ delete amenity object based on its id"""
    amenity = storage.get(Amenity, a_id)
    if amenity:
        amenity.delete()
        storage.save()
        return jsonify({}), 200
    abort(404)


@app_views.route('/amenities', strict_slashes=False, methods=['POST'])
def create_amenity():
    """using method post create amenity"""
    try:
        amenity = request.get_json()

        if amenity.get("name") is None:
            return abort(400, 'Missing name')
    except Exception as e:
        return abort(400, 'Not a JSON')

    new_amen = Amenity(**amenity)
    storage.new(new_amen)
    storage.save()
    return jsonify(new_amen.to_dict()), 201


@app_views.route('/amenities/a_id', strict_slashes=False, methods=['PUT'])
def put_new(a_id):
    """amenity with given id"""
    amen = storage.get(Amenity, a_id)
    if amen:
        try:
            amenity = request.get_json()

            if amenity.get("name") is None:
                return abort(400, 'Missing name')
        except Exception as e:
            return abort(400, 'Not a JSON')

        for key, value in amenity.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amen, key, value)
    
        storage.save()
        return jsonify(amen.to_dict()), 200
    return abort(404)
