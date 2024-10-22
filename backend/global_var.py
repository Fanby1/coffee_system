import configparser
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

config = configparser.ConfigParser()
config.read('config.ini')

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
jwt = JWTManager()