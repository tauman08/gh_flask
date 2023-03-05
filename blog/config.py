class Config:
    DEBUG = False
    DATABASE_URI = ''
    SECRET_KEY = '_5#y2L"F4Q8zFGFGDScvvx54687'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
class Development(Config):
    DEBUG = True

