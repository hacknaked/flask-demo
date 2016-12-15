# coding=utf-8

import os

API_PREFIX = '/api/{}'.format(os.getenv('API_VERSION'))
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True
CSRF_SESSION_KEY = os.getenv('SECRET_KEY')
DATABASE_CONNECT_OPTIONS = {}
DEBUG = True
SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = \
    'postgresql://{user}:{password}@{server}:{port}/{db}'.format(
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        server=os.getenv('POSTGRES_SERVICE'),
        port=os.getenv('POSTGRES_PORT'),
        db=os.getenv('POSTGRES_DB')
    )
SQLALCHEMY_TRACK_MODIFICATIONS = False



