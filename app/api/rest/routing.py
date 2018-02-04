"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""
from flask import request, jsonify, abort
from app.api.rest.base import BaseResource, rest_resource

@rest_resource
class ResourceOneApi(BaseResource):
    """ /api/resources/one """
    endpoints = ['/resources/one/']

    def get(self):
        abort(500)