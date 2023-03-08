import os

from dotenv import load_dotenv

from blog.enums import EnvType

load_dotenv()

ENV = os.getenv('FLASK_ENV', default=EnvType.production)
DEBUG = ENV == EnvType.development

SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False




# class BaseConfig:
#     DEBUG = False
#     DATABASE_URI = ''
#     SECRET_KEY = '_5#y2L"F4Q8zFGFGDScvvx54687'
#
#     SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#
# class Development(BaseConfig):
#     DEBUG = True
#
#
# class TestingConfig(BaseConfig):
#     pass
#
#
# class ProductionConfig(BaseConfig):
#     pass