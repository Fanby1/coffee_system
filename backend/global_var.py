import configparser

config = configparser.ConfigParser()
config.read('config.ini')

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()