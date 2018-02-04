""" API Blueprint Application """

import os
from flask import Flask, Blueprint, session
from flask_restful import Api

api_bp = Blueprint('api_bp', __name__,
                   template_folder='templates',
                   url_prefix='/api')

api_rest = Api(api_bp)

from app.api import views
from app.api.rest import routing
