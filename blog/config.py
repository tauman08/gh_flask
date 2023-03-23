class BaseConfig:
    DEBUG = False
    DATABASE_URI = ''
    SECRET_KEY = '_5#y2L"F4Q8zFGFGDScvvx54687'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WTF_CSRF_ENABLED = True
    FLASK_ADMIN_SWATCH = 'journal'

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


