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
        risk_types = RiskType.get_all()
        return jsonify({'riskTypes': [risk.serialize() for risk in risk_types]})


@rest_resource
class RiskTypeApi(BaseResource):
    """ /api/risk-types/<int:id> """
    endpoints = ['/risk-types/<int:id>']

    def get(self, id):
        risk = [risk for risk in RiskType.get_all() if risk.id == id]
        if len(risk) == 0:
            abort(404)
        return jsonify({'riskType': risk[0].serialize()})
