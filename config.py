import os

class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URI', 'postgresql://localhost/flaskmovies2')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestConfig(DevelopmentConfig):
    TESTING = True
