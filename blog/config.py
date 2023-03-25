import os 
class BaseConfig:
    DEBUG = False
    DATABASE_URI = ''
    SECRET_KEY = '_5#y2L"F4Q8zFGFGDScvvx54687'
    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


    WTF_CSRF_ENABLED = True

    FLASK_ADMIN_SWATCH = 'pulse'

    OPENAPI_URL_PREFIX = '/api/docs'
    OPENAPI_VERSION = '3.0.0'
    OPENAPI_SWAGGER_UI_PATH = '/'
    OPENAPI_SWAGGER_UI_VERSION = '3.51.1'  # see version on https://cdnjs.com/libraries/swagger-ui


class Development(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


# import os

# from dotenv import load_dotenv

# from blog.enums import EnvType

# load_dotenv()

# ENV = os.getenv('FLASK_ENV', default=EnvType.production)
# DEBUG = ENV == EnvType.development

#SECRET_KEY = os.getenv('SECRET_KEY','secret key for my project')
#SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','sqlite:///db.sqlite')


