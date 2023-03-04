from flask import Blueprint

user = Blueprint('user', __name__, url_prefix='users', static_folder='../static' )

@user.route('/')
def user_list():
    return 'Hello'