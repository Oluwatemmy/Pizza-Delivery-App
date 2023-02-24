import os
from decouple import config
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = config('SECRET_KEY', 'secret')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    # SQLALCHEMY_DATABASE_URI = config('DATABASE_URL')   # to run on heroku
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')   # to run locally
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3') or os.environ.get('DATABASE_URL')   # to run locally

class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

class ProdConfig(Config):
    pass

config_dict = {
    'dev': DevConfig,
    'prod': ProdConfig,
    'test': TestConfig
}