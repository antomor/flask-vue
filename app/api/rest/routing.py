"""
REST API Resource Routing

http://flask-restful.readthedocs.io/en/latest/
"""
from flask import request, jsonify, abort
from app.api.rest.base import BaseResource, rest_resource
from app.api.models.risk_types import RiskType


@rest_resource
class RiskTypesApi(BaseResource):
    """ /api/risk-types/ """
    endpoints = ['/risk-types/']

    def get(self):
        abort(500)
