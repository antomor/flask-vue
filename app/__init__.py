from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__, static_url_path='')

from . import config
db = SQLAlchemy(app)

from app.api import api_rest, api_bp
from app.client import client_bp
app.register_blueprint(api_bp)
app.register_blueprint(client_bp)


app.logger.info('>>> {}'.format(app.config['MODE']))


