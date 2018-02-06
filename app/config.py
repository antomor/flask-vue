""" Global Flask Application Settings """

import os
from app import app


class Config(object):
    DEBUG = False
    TESTING = False
    PRODUCTION = False


class Development(Config):
    MODE = 'Development'
    DEBUG = True
    SECRET_KEY = 'SuperSecretKey'


class Testing(Config):
    MODE = 'Testing'
    TESTING = True
    DEBUG = True


class Production(Config):
    MODE = 'Production'
    DEBUG = False
    PRODUCTION = True
    # SECRET_KEY = os.environ['SECRET_KEY']


# Set FLASK_CONFIG env to 'Production' or 'Development' to set Config
flask_config = os.environ.get('FLASK_CONFIG', 'Development')
app.config.from_object('app.config.{}'.format(flask_config))

db_uri = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:////tmp/flask-vue.db')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.logger.info('>>> Database: {}'.format(app.config['SQLALCHEMY_DATABASE_URI']))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False