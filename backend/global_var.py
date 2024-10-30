import configparser
from flask_jwt_extended import JWTManager

config = configparser.ConfigParser()
config.read('config.ini')

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
jwt = JWTManager()